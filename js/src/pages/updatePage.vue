<template>
    <HeaderComp/>
    <h1>Welcome to Update Page</h1>
    <form id="updateStudentForm">
    <input
      type="text"
      id="studentName"
      placeholder="Name"
      v-model="studentName"
      required
    />
    <input
      type="number"
      id="studentGrade"
      placeholder="Grade"
      v-model="studentGrade"
      required
    />
    <button @click="updateStudent()" type="button">Update Student</button>
  </form>
    <FooterComp />
</template>

<script>
    import HeaderComp from '@/components/HeaderComp.vue';
    import FooterComp from '@/components/FooterComp.vue';
        export default{
            name:'updatePage',
            components:{
                HeaderComp,
                FooterComp
            },
            data(){
                return{
                    studentName:'',
                    studentGrade:''
                }
            },
            methods: {
                async updateStudent(){
                    let id = this.$route.params.id
                    const response = await fetch(`http://localhost:8000/students/${id}`,{
                        method: "PUT",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            name: this.studentName,
                            grade: this.studentGrade,
                        }),
                    });
                    if (response.status ==200){
                        alert("student updated successfully");
                        this.$router.push({name:'Home'})
                    }
                }
            },

            async mounted(){

                if (!localStorage.getItem('user')){
                    this.$router.push({name:'SignUp'})
                }
                
                let id = this.$route.params.id
                const response = await fetch(`http://localhost:8000/students/${id}`, {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                    },
                }); 
                const data = await response.json()  
                this.studentName = data[0].name;
                this.studentGrade = data[0].grade;
            },
        }
            
            
</script>