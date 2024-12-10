<template>
  <div class="card-header card-chat-header msg_head" :class="{ 'minimized-header': isMinimized }">
    <div class="d-flex justify-content-between align-items-center w-100">
      <div v-show="!isMinimized">
        <img :src="ImageHeader" class="user_img">
        <span class="user_info_maximized">{{ config.title }}</span>
      </div>
      <div class="user_info_minimized" v-show="isMinimized">
        <span>Nói chuyện với virtual assistant</span>
      </div>
      <button @click="$emit('toggle-chatbot')" class="btn-minimize ml-auto">
        <img :src="isMinimized ? 'maximize_icon.svg' : 'minimize_icon.svg'" alt="Toggle">
      </button>
    </div>
  </div>
</template>

<script>


export default {
  name: "ChatHeader",
  props: {
    ImageHeader: {
      type: String,
      required: true,
    },
    config: {
      type: Object,
      required: true,
    },
    isMinimized: {
      type: Boolean,
      required: true,
    },
    handsFreeFlag: {
      type: Boolean,
      required: true,
    },
  },
};
</script>