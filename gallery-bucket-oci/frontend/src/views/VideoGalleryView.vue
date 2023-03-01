<template>
  <div class="home">
    <VideoGallery msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import VideoGallery from '@/components/VideoGallery.vue'

export default {
  name: 'VideoGalleryView',
  components: {
    VideoGallery
  }
}
</script>