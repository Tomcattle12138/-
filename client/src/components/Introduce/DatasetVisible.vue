<template>
    <div id="app">
      <el-row id="title_div"> 数据可视化 </el-row>
      <div id="help_text">输入货币转化类型和区间，绘制折线图:</div>
  
      <el-input
        v-model="form.slug"
        placeholder="货币转换类型(A/B)"
        class="input"
      ></el-input>
      <time-bar
        :placeholder="'开始时间'"
        @timeupdate="beginTimeUpdate"
      ></time-bar>
      <time-bar :placeholder="'结束时间'" @timeupdate="endTimeUpdate"></time-bar>
      <el-row style="margin-top: 10px">
        <el-button
          type="primary"
          style="font-size: 18px"
          @click="post_plot_request"
        >
          提交
        </el-button>
      </el-row>
      <plot
        v-if="show_plot"
        style="width: 100%; height: 600px"
        :width="24"
        :high="high"
        :low="low"
        :open="open"
        :close="close"
        :title="title"
        :date="date"
        :slug="slug"
      ></plot>
    </div>
  </template>
  
  <script>
  import Vue from "vue";
  import ElementUI from "element-ui";
  import "element-ui/lib/theme-chalk/index.css";
  import Plot from "../Utils/Plot.vue";
  import TimeBar from "../TimeBar.vue";
  
  Vue.use(ElementUI);
  import axios from "axios";
  Vue.prototype.$axios = axios;
  export default {
    name: "Introduce",
    components: {
      TimeBar,
      Plot
    },
    data() {
      return {
        form: {
          slug: "",
          begin_time: "",
          end_time: "",
        },
        show_plot: false,
        title: "汇率变化趋势",
        slug: "",
        date: [],
        high: [],
        low: [],
        close: [],
        open: [],
      };
    },
    methods: {
      post_plot_request() {
        var that = this;
        this.$axios.post("/api/introduce", this.form).then(
          (res) => {
            res = res.data;
            that.slug = res.slug;
            that.date = res.date;
            that.high = res.high;
            that.open = res.open;
            that.close = res.close;
            that.low = res.low;
            that.show_plot = true;
          },
          (error) => {
            console.log(error);
          }
        );
      },
      beginTimeUpdate(begin_time) {
        this.form.begin_time = begin_time;
      },
      endTimeUpdate(end_time) {
        this.form.end_time = end_time;
      },
    },
  };
  </script>
  
  <style scoped>
  #app {
    width: 80%;
    margin-left: 10%;
  }
  #title_div {
    text-align: center;
    font-size: 35px;
    font-family: 方正书宋体;
    font-weight: bold;
  }
  
  .input {
    width: 200px;
    margin-top: 10px;
  }
  
  #help_text {
    width: 100%;
    font-size: 20px;
    font-family: "微软雅黑";
    margin-top: 20px;
  }
  </style>