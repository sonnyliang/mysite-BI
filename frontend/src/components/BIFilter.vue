<template>
<form>
    <div class="form-group">
        <label for="exampleSelect1">分析维度</label>
        <select class="form-control" id="exampleSelect1" v-model='col'>
            <option>品牌</option>
            <option>大区</option>
        </select>
        <select class="form-control" id="exampleSelect1" v-model='row'>
            <option>订单日期</option>
        </select>
        <select class="form-control" id="exampleSelect1" v-model='pivot_value'>
            <option>销售额</option>
            <option>消费人数</option>
        </select>
    </div>

    <div class="form-group">
        <label for="exampleSelect1">数据筛选</label>
        <div class="field">
            <select class="form-control" id="exampleSelect2" v-model='brand'>
                <option>CHJ</option>
                <option>CH</option>
                <option>FION</option>
                <option>VENTI</option>
                <option>ALL</option>
            </select>
        </div>
        <br>
        <div class="container">
            <div class="row">
                订单开始日期：
                <div class="col-md-6">
                    <date-picker
                        v-model="startDate"
                        :config="options"
                        @dp-hide="showDatePickResult"/>
                </div>
                订单结束日期：
                <div class="col-md-6">
                    <date-picker
                        v-model="endDate"
                        :config="options"
                        @dp-hide="showDatePickResult"/>
                </div>
            </div>
        </div>
    </div>
    
    <button type="button" class="btn btn-primary" @click='getPivot'>Submit</button>
    <button type="button" class="btn btn-primary" @click='sendData'>向父组件传数据</button>
</form>
</template>

<script>
import datePicker from 'vue-bootstrap-datetimepicker'
import $ from 'jquery'
import axios from 'axios'

export default {
	name: 'BIFilter',
	data () {
		return {
            pivot_value:'amount',
            col:'brand',
            row:'billdate',
            brand:'CHJ',
            startDate: new Date(),
            endDate: new Date(),
			options: {
				format: 'YYYY-MM-DD',
				useCurrent: false,
				locale: 'zh-cn',
				tooltips: {
                selectTime: ''
                },
            },
            sendValue:'向父组件传的数据',
            updateData:[],
		}
	},
	methods: {
		showDatePickResult: function () {
			console.log(this.startDate)
        },
        showParam: function(){
            console.log({'brand':this.brand,
                            'startDate':this.startDate,
                            'endDate':this.endDate,
                            'col':this.col,
                            'row':this.row,
                            'value':this.pivot_value,
                            })
        },
        getPivot:function(){
            axios.get('/bi/api/paramtest',
                        {params:{'brand':this.brand,
                        'startDate':this.startDate,
                        'endDate':this.endDate,
                        'col':this.col,
                        'row':this.row,
                        'value':this.pivot_value,
                        }}).then(res =>{
                            this.updateData=res.data;
                            console.log(this.updateData);
                            this.sendData();
                            })
        },
        sendData:function(){
            this.$emit("testValue",this.updateData);
        }
	},
	components: {
		datePicker
	},
	created: function () {
		$.extend(true, $.fn.datetimepicker.defaults, {
            icons: {
            time: 'far fa-clock',
            date: 'far fa-calendar',
            up: 'fas fa-arrow-up',
            down: 'fas fa-arrow-down',
            previous: 'fas fa-chevron-left',
            next: 'fas fa-chevron-right',
            today: 'fas fa-calendar-check',
            clear: 'far fa-trash-alt',
            close: 'far fa-times-circle'
            }
        })
	}
}
</script>