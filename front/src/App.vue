<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style>

body{
  padding: 2%;
}

b-button{
padding-top: 5%;
padding-bottom: 5%;
}

#button {
  transition-duration: 0.4s;
  text-decoration: none;
  border-radius: 4px;
  color: #ff4d4d;
  padding: 0.5%;
  border: solid 2px #ff4d4d;
}

#button:hover {
  background-color: #ff4d4d; /* red */
  color: white;
}

</style>
