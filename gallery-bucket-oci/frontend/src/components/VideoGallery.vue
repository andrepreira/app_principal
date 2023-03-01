<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div class="container">
      <h1>Video Gallery</h1>
      <div class="row">
        <div v-for="(videoUrl, index) in videoUrls" :key="index" class="col-md-4 mb-3">
            <video class="img-fluid" controls v-if="videoUrl">
                <source :src="videoUrl" type="video/mp4">
            </video>
        </div>
      </div>
    </div>
  </template>
  
<script>

import axios from 'axios';
  
export default {
    name: 'VideoGallery',
    data() {
          return {
              videoUrls: [],
            };
        },
        created() {
            axios.get('http://backend:5000/api/videos')
                .then(response => {
                    this.videoUrls = response.data.videos;
                    console.log(response.data.videos);
                })
                .catch(error => {
                    console.error(error);
                });
        },
}
  
</script>