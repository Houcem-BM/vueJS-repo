<template>
  <HeaderComp />
  <h1>Add Student</h1>
  <div id="addStudentForm">
    <input
      type="text"
      id="studentName"
      placeholder="Name"
      v-model="student_name"
      required
    />
    <input
      type="number"
      id="studentGrade"
      placeholder="Grade"
      v-model="student_grade"
      required
    />
    <button @click="addStudent()" type="button">Add Student</button>
  </div>
  <FooterComp />
</template>

<script>
import HeaderComp from "../components/HeaderComp.vue";
import FooterComp from "../components/FooterComp.vue";
export default {
  name: "AddStudent",
  components: {
    HeaderComp,
    FooterComp,
  },
  data() {
    return {
      student_name: "",
      student_grade: ""
    };
  },
  methods: {
    async addStudent() {
      const response = await fetch(`http://localhost:8000/students/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: this.student_name,
          grade: this.student_grade
        }),
      });
      if (response.status == 200){
        alert(" Student added successfuly")
        this.$router.push({name:'Home'})
      }
    },
  },
  mounted(){
    if (!localStorage.getItem("user")){
      this.$router.push({name:'Login'})
    }
  }
};
</script>

<style scoped>
#addStudentForm{
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin: 20px auto 0;
  padding: 15px;
  background-color: #ffffff;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  width: 40%;
}
</style>
