import torch
import json
from argparse import ArgumentParser
import sys
sys.path.append('../')
from models.timegan import TimeGAN

parser = ArgumentParser()
args = parser.parse_args()
args.Z_dim = 4
args.dis_thresh=0.15
args.feature_dim=4
args.hidden_dim=20
args.max_seq_len=100
args.num_layers=3
args.padding_value=-1.0
args.device='cpu'
args.batch_size=128
gan_model = TimeGAN(args)

gan_model.load_state_dict(torch.load('./state_dict/timegan_state_dict.pkl', map_location=torch.device('cpu')))
print("load TimeGAN model successfully!")

def finishwork():
    graphs_json_data = json.load(open('./JSON/real_generate_graphs.json', 'r'))
    return graphs_json_data

def timegan_generator(model, test_data, T, args):  # 根据text_data前半段进行生成
    model.eval()
    with torch.no_grad():
        # Generate fake data
        Z = torch.rand((len(T), args.max_seq_len, args.Z_dim))
        Z = torch.cat([test_data[:, :10, :], Z[:, 10:, :]], dim=1)
        generated_data = model(X=None, T=T, Z=Z, obj="inference")
    generated_data = torch.cat([test_data[:,:10,:],generated_data[:,10:,:]],dim=1)
    return generated_data

def predict(open, high, low, close):
    currency_list = open + ',' + high + ',' + low + ',' + close
    arr = [float(num) for num in currency_list.split(',')]
    arr = torch.tensor(arr).reshape(4,-1).T  # [10,4]
    params = torch.tensor([[5.863,6.04,5.8574,5.863],[8.28,8.297,8.2775,8.2777]])
    arr = (arr - params[0]) / (params[1] - params[0])
    T = [24]
    arr = arr.unsqueeze(0)
    ans = timegan_generator(gan_model, arr, T, args)[0,:24]
    ans = ans * (params[1] - params[0]) + params[0]
    open_ = ans[:,0].tolist()
    high = ans[:,1].tolist()
    low = ans[:,2].tolist()
    close = ans[:,3].tolist()
    ans_json = {
        'open': open_,
        'high': high,
        'low': low,
        'close': close
    }
    return ans_json