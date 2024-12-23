<template>
  <router-view/>
  
</template>

<script>
export default {
  name:'App',
  
}



</script>
<style>
body{
  margin: 0;
  padding: 0;
}
.container {
  margin:80px auto 0;
  text-align: center;
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 300px;
}

.logo {
max-width: 100px;
margin-bottom: 20px;
}

h1 {
font-size: 24px;
margin-bottom: 20px;
color: #333;
}

        form {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-top: 20px;
            padding: 15px;
            background-color: #ffffff;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }

        input{
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 14px;
            margin: 10px 5px;
            padding: 10px 12px;
            font-size: 14px;
            outline: none;
          }
        input:focus {
            border-color: #4a90e2;
            box-shadow: 0 0 5px rgba(74, 144, 226, 0.5);
          }

        button {
            padding: 10px;
            background-color: #4a90e2;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 17px;
            transition: background-color 0.3s ease;
            margin-right:10px;
        }

        button:hover {
            background-color: #45a049;
        }
        nav {
            background-color: #333;
            overflow: hidden;
          }

        nav a {
            color: #f2f2f2f2;
            float: left;
            padding: 14px 16px;
            text-align: center;
            text-decoration: none;
            margin-right: 5px;
            font-size: 17px;
          }

        nav a:hover {
            background-color: #ddd;
            color: #333;
          }
        .input-error {
            border: 2px solid red;
          }

        .error-message {
          color: red;
          font-size: 12px;
          margin-top: 2px;
        }
</style>
