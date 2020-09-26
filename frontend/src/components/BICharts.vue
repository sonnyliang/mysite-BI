<template>
  <div>
    <!-- 折线图的视图展示层，双向绑定chartData进行数据填充 -->
    <!-- 双向绑定settings，进行一些设置 -->
    <ve-line :data="chartData" :settings="chartSettings"></ve-line>
    测试
    <div v-for="(item, index, key) in testRows" :index=index :key=key>{{key}}</div>
  </div>
</template>

<script>
    export default{
      data: function () {
        return {
          chartData: {
            chartSettings:{
              labelMap:{
                //data对应后台返回json数据的key，具体值根据接口字段来修改
                date:'日期',
                //total对应后台返回json数据的value，具体值根据接口阶段来修改
                total:'商户数量'
              }
            },
            chartData:{
              // 这里的格式必须是对应上面后台接口的字段才能显示图例
              columns: ['日期', '销售额'],
              rows: {}
            }
          },
          testRows:[
            { '日期': '1月1日', '销售额': 123 },
            { '日期': '1月2日', '销售额': 1223 },
            { '日期': '1月3日', '销售额': 2123 },
            { '日期': '1月4日', '销售额': 4123 },
            { '日期': '1月5日', '销售额': 3123 },
            { '日期': '1月6日', '销售额': 7123 }
          ],
        }
      },
      method:function(){ 
      }
    }
</script>