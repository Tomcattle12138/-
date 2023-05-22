
<template>
    <el-col :span="width">
      <div ref="chart" style="width: 100%; height: 600px"></div>
    </el-col>
</template>

<script>
import ElementUI from "element-ui";
import Vue from "vue";
Vue.use(ElementUI);

import * as echarts from "echarts";
Vue.prototype.$echarts = echarts;

export default {
  name: "Plot",
  props: {
    width: {
      type: Number,
      default: () => 24,
    },
    title: "",
    slug: "",
    date: {
      type: Array,
      default: () => [],
    },
    high: {
      type: Array,
      default: () => [],
    },
    open: {
      type: Array,
      default: () => [],
    },
    low: {
      type: Array,
      default: () => [],
    },
    close: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      MyChart: "",
    };
  },
  methods: {
    get_mn() {
      var mn = Math.min(...this.low).toFixed(2)
      return mn
    },
    getEchartData() {
      const chart = this.$refs.chart;
      if (chart) {
        const myChart = this.$echarts.init(chart);
        this.MyChart = myChart;
        myChart.setOption(this.chartOptions);
      }
    },
  },
  watch: {
    high(new_high, old_high) {
      var chart = this.$refs.chart;
      this.MyChart.setOption(this.chartOptions);
      console.log(this.chartOptions);
      console.log("redraw plot");
    },
  },
  mounted() {
    this.getEchartData();
  },
  computed: {
    chartOptions: function () {
      return {
        // Echarts options here...
        title: {
          text: this.title,
          left: "center",
        },
        tooltip: {},
        xAxis: {
          data: this.date,
        },
        yAxis: {
          min: this.get_mn(),
        },
        series: [
          {
            name: "open",
            type: "line",
            data: this.open,
            lineStyle: {
              color: "#ffaa00",
            },
          },
          {
            name: "high",
            type: "line",
            data: this.high,
            lineStyle: {
              color: "#ff0000",
            },
          },
          {
            name: "low",
            type: "line",
            data: this.low,
            lineStyle: {
              color: "#000000",
            },
          },
          {
            name: "close",
            type: "line",
            data: this.close,
            lineStyle: {
              color: "#5500ff",
            },
          },
        ],
      };
    },
  },
};
</script>