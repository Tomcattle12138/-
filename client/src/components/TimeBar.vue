<template>
    <span class="block" style="margin-left:10px">
      <el-date-picker
        v-model="value1"
        type="date"
        :placeholder="placeholder" @input="updateTime" value-format="yyyy-MM-dd">
      </el-date-picker>
    </span>
</template>

<script>
import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)

export default {
props:{
  placeholder: ''
},
data() {
    return {
    pickerOptions: {
        disabledDate(time) {
        return time.getTime() > Date.now();
        },
        shortcuts: [{
        text: '今天',
        onClick(picker) {
            picker.$emit('pick', new Date());
        }
        }, {
        text: '昨天',
        onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24);
            picker.$emit('pick', date);
        }
        }, {
        text: '一周前',
        onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
            picker.$emit('pick', date);
        }
        }]
      },
      value1: ''
    };
},
methods: {
  updateTime(){
    this.$emit('timeupdate', this.value1)
  }
}
};
</script>