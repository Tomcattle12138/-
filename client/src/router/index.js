import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ShowFinishWork from '../components/MediumRegression/ShowFinishWork.vue'
import MediumRegression from '../components/MediumRegression/MediumRegression.vue'
import TestOnline from '../components/MediumRegression/TestOnline.vue'
import Introduce from "@/components/Introduce/Introduce.vue"
import DatasetVisible from "@/components/Introduce/DatasetVisible.vue"
import DatasetIntroduce from "@/components/Introduce/DatasetIntroduce"
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    redirect: '/introduce/dataset_introduce'
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/introduce',
    name: 'introduce',
    component: Introduce,
    children: [
      {
        path: '',
        redirect: 'dataset_introduce'
      },
      {
        path: 'dataset_introduce',
        name: 'dataset introduce',
        component: DatasetIntroduce
      },
      {
        path: 'dataset_visible',
        name: 'dataset visible',
        component: DatasetVisible
      }
    ]
  },
  {
    path: '/medium_regression',
    name: 'medium_regression',
    component: MediumRegression,
    children: [
      {
        path: '',
        redirect: 'show_finishwork'
      },
      {
        path: 'show_finishwork',
        name: 'show finishwork',
        component: ShowFinishWork
      },
      {
        path: 'test_online',
        name: 'test online',
        component: TestOnline
      },
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
