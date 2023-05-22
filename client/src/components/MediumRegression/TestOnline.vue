<template>
  <div>
    <el-row>
      <el-col :span="12" :offset="6" style="margin-top: 10px;">
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="open">
            <el-input v-model="form.open"></el-input>
          </el-form-item>
          <el-form-item label="high">
            <el-input v-model="form.high"></el-input>
          </el-form-item>
          <el-form-item label="low">
            <el-input v-model="form.low"></el-input>
          </el-form-item>
          <el-form-item label="close">
            <el-input v-model="form.close"></el-input>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
    <el-row>
        <el-col :span="4" :offset="10" style="margin-top: 10px">
      <input
        type="file"
        ref="fileInput"
        v-show="false"
        accept=".txt,.csv"
        @input="onFileInputChange"
      />
      <el-button @click="choose_file" type="success"> 选择文件 </el-button>
      <el-button type="primary" @click="get_predict_data">提交</el-button>
        </el-col>
    </el-row>

    <plot
      title="汇率预测结果"
      :high="high"
      :low="low"
      :close="close"
      :open="open"
      v-if="show_plot"
    ></plot>
  </div>
</template>

<script>
import ElementUI from "element-ui";
import Vue from "vue";
import axios from "axios";
import Plot from "../Utils/Plot.vue";
Vue.use(ElementUI);

export default {
  data() {
    return {
      close: [],
      high: [],
      open: [],
      low: [],
      show_plot: false,
      form: {
        high: "",
        low: "",
        open: "",
        close: "",
      },
    };
  },
  components: {
    Plot,
  },
  methods: {
    get_predict_data() {
      var that = this;
      axios
        .post("/api/medium_regression/test_online", {
          open: this.form.open,
          close: this.form.close,
          high: this.form.high,
          low: this.form.low,
        })
        .then(
          (res) => {
            res = res.data;
            that.close = res.close;
            that.high = res.high;
            that.open = res.open;
            that.low = res.low;
            that.show_plot = true;
          },
          (error) => {
            alert(error);
          }
        );
    },
    choose_file() {
      this.$refs.fileInput.click();
    },
    onFileInputChange(event) {
      const file = event.target.files[0];
      const reader = new FileReader();
      reader.onload = () => {
        var result = reader.result.replace(/\r/g, "");
        var currency_list = result.split("\n");
        this.form.open = currency_list[0];
        this.form.high = currency_list[1];
        this.form.low = currency_list[2];
        this.form.close = currency_list[3];
      };
      reader.readAsText(file);
    },
  },
};
</script>

<style>
.el-form-item__label{
    font-size: 18px;
}
.el-input__inner{
    font-size: 18px;
}
</style>