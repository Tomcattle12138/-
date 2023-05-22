import torch
import torch.nn as nn
import numpy as np
import pandas as pd
import os
import warnings
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, precision_recall_curve
from sklearn.metrics import recall_score, f1_score, roc_curve
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
# gpu
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
device = torch.device('cuda')

df = pd.read_csv('forex.csv')
df = df[:10000]

scaler = MinMaxScaler(feature_range=(-1, 1)) 
for col in ['open', 'high', 'low', 'close']:
    df[col] = scaler.fit_transform(df[col].values.reshape(-1, 1))

X, y = [], []
for i in range(10, len(df)):
    X.append(df[['open', 'high', 'low', 'close']][i-10:i])
    y.append(1 if df['close'][i] > df['open'][i-1] else 0)
X, y = np.array(X), np.array(y)

train_size = int(len(X)*0.7)
X_train, y_train = X[:train_size], y[:train_size]
X_test, y_test = X[train_size:], y[train_size:]

class StockLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(input_size, hidden_size)
        self.fc = nn.Linear(hidden_size, output_size)
        
    def forward(self, x):
        batch_size = 10
        hidden = (torch.zeros(1, batch_size, self.hidden_size).to(device),
                  torch.zeros(1, batch_size, self.hidden_size).to(device))
        out, hidden = self.lstm(x, hidden)
        out = self.fc(out[:, -1, :])
        return out
    
# 定义模型参数
input_size = 4
hidden_size = 32
output_size = 1

# 定义模型和优化器
model = StockLSTM(input_size, hidden_size, output_size).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# 训练模型
num_epochs = 400
batch_size = 256

for epoch in range(num_epochs):
    for i in range(0, len(X_train), batch_size):
        x_batch = torch.tensor(X_train[i:i+batch_size], dtype=torch.float32).to(device)
        y_batch = torch.tensor(y_train[i:i+batch_size], dtype=torch.float32).to(device)
        
        # 前向传播
        y_pred = model(x_batch)
        
        # 计算损失
        loss = nn.BCEWithLogitsLoss()(y_pred.squeeze(), y_batch)
        
        # 反向传播和优化
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    # 打印训练过程
    if (epoch+1) % 10 == 0:
        with torch.no_grad():
            x_test = torch.tensor(X_test, dtype=torch.float32).to(device)
            y_test = torch.tensor(y_test, dtype=torch.float32).to(device)
            y_pred = model(x_test)
            test_loss = nn.BCEWithLogitsLoss()(y_pred.squeeze(), y_test)
            print(f'Epoch [{epoch+1}/{num_epochs}], Train Loss: {loss.item():.4f}, Test Loss: {test_loss.item():.4f}')
    
# 在测试集上评估模型
with torch.no_grad():
    test_losses = []
    y_preds = []
    x_batch = torch.tensor(X_test, dtype=torch.float32).to(device)
    y_batch = torch.tensor(y_test, dtype=torch.float32).to(device)
    y_pred = model(x_batch)
    test_loss = nn.BCEWithLogitsLoss()(y_pred.squeeze(), y_batch)
    test_losses.append(test_loss.item())
    y_preds.append(torch.sigmoid(y_pred).cpu().numpy())

    test_loss = np.mean(test_losses)
    y_preds = np.concatenate(y_preds)

print('Test Loss: ', test_loss)
y_pred = []
for pred in y_preds:
    y_pred.append(pred[0])
y_pred = np.array(y_pred)
y_res = [0 if pred < 0.5 else 1 for pred in y_pred]
print('Predict: ', y_res)
y_test = y_test.cpu().numpy()

print('Accuracy: ', accuracy_score(y_test, y_res))
print('Precision: ', precision_score(y_test, y_res))
print('Recall: ', recall_score(y_test, y_res))
print('F1: ', f1_score(y_test, y_res))
fpr, tpr, thresholds = roc_curve(y_test, y_pred)
plt.figure()
plt.plot(fpr, tpr)
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.title('ROC Curve')
plt.savefig('ROC_Curve.png')

precision, recall, thresholds = precision_recall_curve(y_test, y_pred)
plt.figure()
plt.title('Precision/Recall Curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.plot(recall, precision)
plt.savefig('PR_Curve.png')
