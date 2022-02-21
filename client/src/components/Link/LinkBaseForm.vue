<script setup>
import { ref, computed, reactive } from "vue";
import apiFetch from "~/plugins/apiFetch.js";
const emit = defineEmits({
  refresh: null,
});
const props = defineProps({
  item: {
    type: Object,
    default: () => ({
      id: null,
      link_origin: "",
      expires_dt: "",
      is_active: true,
    }),
  },
  blank: {
    type: Boolean,
    default: false,
  },
});
let editMode = ref(props.blank);
const link = reactive({ ...props.item });
const daysLeft = computed({
  get() {
    if (link.expires_dt.length < 1) {
      link.expires_dt = nowPlusNDaysIso(90 + 1);
      return 90;
    }
    return utilDaysLeft(link.expires_dt);
  },
  set(newValue) {
    link.expires_dt = nowPlusNDaysIso(newValue + 1);
  },
});

function utilDaysLeft(date) {
  const msSecInDay = 60 * 60 * 24 * 1000;
  const leftSeconds = new Date(date) - Date.now();
  return parseInt(leftSeconds / msSecInDay);
}
function nowPlusNDaysIso(days) {
  const dt = new Date();
  dt.setDate(dt.getDate() + days);
  return dt.toISOString();
}
async function send() {
  if (link.id != null) {
    let res = await apiFetch(`/link/${props.item.link_short}`, {
      method: "PUT",
      body: link,
    });
    editMode.value = props.blank ? true : false;
    emit("refresh");
  } else {
    // create new one
    try {
      const res = await apiFetch("/link/", { method: "POST", body: link });
      emit("refresh");
    } catch (error) {}
  }
}
async function remove() {
  try {
    await apiFetch(`/link/${link.link_short}`, {
      method: "DELETE",
    });
    emit("refresh");
  } catch (error) {}
}
</script>

<template lang="pug">
form.link-form(@submit.prevent="send")
  input.checkbox(type="checkbox" v-model='link.is_active'  :disabled='!editMode')
  input.input.origin(v-model.trim='link.link_origin' placeholder="Enter valid url"  :disabled='!editMode')
  input.input.short(v-if='link.id && editMode' v-model.trim='link.link_short' :disabled='!editMode')
  a.short(v-if='link.id && !editMode' target='_blank' :href="`http://localhost:8000/${link.link_short}`", v-html="`http://localhost:8000/${link.link_short}`" )
  input.input.num(type='number' v-model.lazy='daysLeft' min=1 max=365 :disabled='!editMode')
  .actions.buttons(v-if='editMode' )
    button.button.is-primary Save
    button.button.is-danger(v-if="!blank" type='button' @click.stop='remove') Remove
  button.button.is-primary(v-else @click.stop='editMode = true') Edit
     
</template>

<style lang="scss">
.link-form {
  @apply 'border-1 border-light-100';
  display: flex;
  align-items: "middle";
  & > * + * {
    @apply "ml-4";
  }
}
.input.num {
  @apply 'max-w-20';
}
.input.short,
a.short {
  @apply 'w-60';
}
input.origin {
  @apply 'w-2/5';
}

.temp {
  @apply 'flex max-w-30 max-w-22 min-w-22';
}
.actions {
  @apply 'min-w-44';
}
</style>
