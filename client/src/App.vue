<script setup>
import { reactive, ref } from "vue";
import LinkBaseForm from "~/components/Link/LinkBaseForm.vue";

import apiFetch from "~/plugins/apiFetch.js";
const links = ref([]);

function fetchAll() {
  console.log("refresh");
  apiFetch("/link/").then((res) => {
    links.value = res;
  });
}

// Init
fetchAll();
</script>

<template lang="pug">
main.main
  .c-container
    h1.title.is-1.has-text-centered hrefy
    h2.title.is-3 Add new link 
    .add-form
      link-base-form(blank @refresh='fetchAll')
    hr
    h2.title.is-3 All links
    .links-item.mt-2(v-for='link in links' :key='link.id')
      link-base-form(:item='link' @refresh='fetchAll')
</template>

<style lang="scss">
html {
  @apply 'font-sans';
}
.c-container {
  @apply "w-11/12 max-w-1280px mx-auto";
}
.add-form {
}
</style>
