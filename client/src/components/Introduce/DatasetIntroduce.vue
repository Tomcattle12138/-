<template>
    <div>
        <el-row>
            <el-col :span="18" :offset="6">
                <h2>数据集: <a href="https://www.kaggle.com/datasets/dhruvildave/currency-exchange-rates">Currency Foreign
                        Exchange Rates</a></h2>
            </el-col>
        </el-row>

        <el-row class="medium_font_size" span="24">
            数据集基本情况： <br />
            数据集分析：
            包含了7个列,分别是
            <el-table :data="tableData" style="width: 100%;margin-top:10px" class="medium_font_size">
                <el-table-column prop="column_name" label="属性" width="300">
                </el-table-column>
                <el-table-column prop="column_meaning" label="含义" width="300">
                </el-table-column>
            </el-table>
        </el-row>
        <el-row style="margin-top:10px;">
            <img :src="dataset_basic_info" alt="图片" />
        </el-row>
        <el-row style="margin-top:10px;">
            <el-col :span="18" class="medium_font_size" style="letter-spacing: 2px">
                经过统计,数据集包含了涉及到113种货币(113种currency/slug_currency, 7种slug_foreign)的340种货币兑换汇率记录。
                统计开始时间为1996年10月30日,统计结束时间为2021年08月30日,共有6445天的记录,每周的记录了周一到周五的汇率变化情况。
                另外,我们发现,存在少量slug_currency与currency不一致的情况。在这些数据中,currency的取值全部为USD,而slug_currency的取值包括
                {'EUR/RON', 'EUR/MGA', 'GBP/ZMW', 'EUR/GHS', 'GBP/RON'}。在处理这些数据时,需要注意这一特例。
            </el-col>
        </el-row>
    </div>
</template>

<script>
import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)
export default {
    data() {
        return {
            dataset_basic_info: require("@/assets/dataset_basic_info.png"),
            tableData: [{
                column_name: 'slug',
                column_meaning: '兑换的两种货币(A货币/B货币)'
            },
            {
                column_name: 'open',
                column_meaning: '开盘价格'
            },
            {
                column_name: 'high',
                column_meaning: '最高价格'
            },
            {
                column_name: 'low',
                column_meaning: '最低价格'
            },
            {
                column_name: 'close',
                column_meaning: '闭盘价格'
            },
            {
                column_name: 'currency',
                column_meaning: '基准货币(A货币/B货币)'
            }
            ]
        }
    }
}
</script>

<style>
.medium_font_size{
    font-size: 18px;
    color: black;
}
</style>
