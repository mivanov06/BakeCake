Vue.createApp({
    name: "App",
    components: {
        VForm: VeeValidate.Form,
        VField: VeeValidate.Field,
        ErrorMessage: VeeValidate.ErrorMessage,
    },
    data() {
        let js_data = JSON.parse(document.getElementById('js_data').textContent);
        let js_costs = JSON.parse(document.getElementById('js_costs').textContent);
        return {
            schema1: {
                lvls: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' количество уровней';
                },
                form: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' форму торта';
                },
                topping: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' топпинг';
                }
            },
            schema2: {
                name: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' имя';
                },
                phone: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' телефон';
                },
                name_format: (value) => {
                    const regex = /^[a-zA-Zа-яА-Я]+$/
                    if (!value) {
                        return true;
                    }
                    if ( !regex.test(value)) {

                        return '⚠ Формат имени нарушен';
                    }
                    return true;
                },
                email_format: (value) => {
                    const regex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i
                    if (!value) {
                        return true;
                    }
                    if ( !regex.test(value)) {

                        return '⚠ Формат почты нарушен';
                    }
                    return true;
                },
                phone_format:(value) => {
                    const regex = /^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$/
                    if (!value) {
                        return true;
                    }
                    if ( !regex.test(value)) {

                        return '⚠ Формат телефона нарушен';
                    }
                    return true;
                },
                email: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' почту';
                },
                address: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' адрес';
                },
                date: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' дату доставки';
                },
                time: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' время доставки';
                }
            },
            DATA: js_data,
            Costs: js_costs,
            Levels: 0,
            Form: 0,
            Topping: 0,
            Berries: 0,
            Decor: 0,
            Words: '',
            Comments: '',
            Designed: false,

            Name: '',
            Phone: null,
            Email: null,
            Address: null,
            Dates: null,
            Time: null,
            DelivComments: ''
        }
    },
    methods: {
        ToStep4() {
            this.Designed = true
            setTimeout(() => this.$refs.ToStep4.click(), 0);
        },
        submitOrder: function(){
            axios({
                method : "POST",
                url:"api/order/", //django path name
                headers: {
                    'X-CSRFTOKEN': document.cookie.match("(^|;)\\s*" + "csrftoken" + "\\s*=\\s*([^;]+)")?.pop(),
                    'Content-Type': 'application/json'
                },
                data : {
                    "Name":this.Name,
                    "Phone":this.Phone,
                    "Email":this.Email,
                    "Address":this.Address,
                    "Dates":this.Dates,
                    "Time":this.Time,
                    "DelivComments":this.DelivComments,
    
                    "Levels":this.Levels,
                    "Form":this.Form,
                    "Topping":this.Topping,
                    "Berries":this.Berries,
                    "Decor":this.Decor,
                    "Words":this.Words,
                    "Comments":this.Comments,
                    "Designed":this.Designed,

                    "components": this.DATA,
                    "prices": this.Costs,
                },//data
            }).then(response => {
                this.success_msg = response.data['msg'];      
            }).catch(err => {
                this.err_msg = err.response.data['err'];
            });        
        }
    },
    computed: {
        Cost() {
//            let date_1 = new Date(2023, 6, 26, 16, 0, 0)
//            let date_2 = new Date(2023, 6, 27, 16, 0, 0)
//            console.log(this)
            let W = this.Words ? this.Costs.Words : 0
            return this.Costs.Levels[this.Levels] + this.Costs.Forms[this.Form] +
                this.Costs.Toppings[this.Topping] + this.Costs.Berries[this.Berries] +
                this.Costs.Decors[this.Decor] + W
        }
    },
}).mount('#VueApp')