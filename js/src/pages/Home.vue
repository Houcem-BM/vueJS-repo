<template>
    <HeaderComp/>
    <h1>Welcome {{ user }}</h1>
    <h2>Student Management</h2>
  
     <!-- Section to display students -->
  <h3>Student List</h3>
  <table id="studentTable">
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Grade</th>
        <th>Actions</th>
      </tr>
      <tr v-for="student in students" :key="student.id">
        <td>{{ student.id }}</td>
        <td>{{ student.name }}</td>
        <td>{{ student.grade }}</td>
        <td> 
          <button type="button"><router-link :to= "'/update/'+ student.id">Update</router-link></button>
          <button @click="Delete(student.id)" type="button">Delete</button>
        </td>
      </tr>
    </thead>
    <tbody>
      <!-- Dynamic content goes here -->
    </tbody>
  </table>

    <FooterComp/>
</template>

<script>
    import HeaderComp from '../components/HeaderComp.vue'
    import FooterComp from '../components/FooterComp.vue'
        export default{
            name:'HomePage',
            components:{
                FooterComp,
                HeaderComp

            },
            data(){
              return{
                students:[],
                user:''
              }
            },
            methods:{
              async Delete(id){
                const response = await fetch (`http://localhost:8000/students/${id}`, {
                  method: "DELETE",
                  headers: {
                      "Content-Type": "application/json",
                    },
              });
              if (response.status == 200){
                alert("student deleted successfully");
                window.location.reload()
              }
              }
            },
            async mounted(){
              let user_name = localStorage.getItem('user')
              if (user_name){
                this.user = user_name
                this.$router.push({name:'Home'})
              }else{
                this.$router.push({name:'SignUp'})
              }

              const response = await fetch ("http://localhost:8000/students/", {
                  method: "GET",
                  headers: {
                      "Content-Type": "application/json",
                    },
              });
              const data = await response.json();
              this.students = data;
            }
        }
</script>

<style>
 h1, h2, h3 {
    color: #4a90e2;
    text-align: center;
  }
    table {
    border-collapse: collapse;
    width: 90%;
    background-color: #ffffff;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
    margin: 0 auto 20px;
  }
  
  th, td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: center;
  }
  
  th {
    background-color: #4a90e2;
    color: #ffffff;
    font-weight: bold;
  }
  
  tr:nth-child(even) {
    background-color: #f1f5f3;
  }
  
  tr:hover {
    background-color: #eaf1f8;
    cursor: pointer;
  }
 
</style>