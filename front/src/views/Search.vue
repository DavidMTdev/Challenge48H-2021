<template>
  <body>
    <div name="button">
      <!-- <b-button variant="outline-danger">New</b-button> -->
      <router-link to="/create">New</router-link>
    </div>

    <h1>Your request</h1>

    <div id="Forms">
      <b-form inline id="bform" @submit="onSubmit">
        <div>
          <div>
            <p>Nom de la photo</p>
            <b-form-input
              v-model="name"
              placeholder="Filename"
            ></b-form-input>
          </div>

          <div>
            <p>Type d'image</p>
            <b-form-input
              v-model="type"
              placeholder="Image type"
            ></b-form-input>
          </div>

          <div>
            <b-form-group
              label="Photo avec produit"
              v-slot="{ ariaDescribedby }"
            >
              <b-form-radio
                v-model="picture_product"
                :aria-describedby="ariaDescribedby"
                name="some-radios"
                value="oui"
                >Oui</b-form-radio
              >
              <b-form-radio
                v-model="picture_product"
                :aria-describedby="ariaDescribedby"
                name="some-radios"
                value="non"
                >Non</b-form-radio
              >
            </b-form-group>
          </div>
        </div>
        <div>
          <div>
            <b-form-group
              label="Photo avec Humain"
              v-slot="{ ariaDescribedby }"
            >
              <b-form-radio
                v-model="picture_human"
                :aria-describedby="ariaDescribedby"
                name="some-radios1"
                value="oui"
                >Oui</b-form-radio
              >
              <b-form-radio
                v-model="picture_human"
                :aria-describedby="ariaDescribedby"
                name="some-radios1"
                value="non"
                >Non</b-form-radio
              >
            </b-form-group>
          </div>

          <div>
            <b-form-group
              label="Photo institutionnelle"
              v-slot="{ ariaDescribedby }"
            >
              <b-form-radio
                v-model="picture_institutional"
                :aria-describedby="ariaDescribedby"
                name="some-radios2"
                value="oui"
                >Oui</b-form-radio
              >
              <b-form-radio
                v-model="picture_institutional"
                :aria-describedby="ariaDescribedby"
                name="some-radios2"
                value="non"
                >Non</b-form-radio
              >
            </b-form-group>
          </div>
        </div>
        <div>
          <div>
            <p>Credits de la photo</p>
            <b-form-input
              v-model="credits"
              placeholder="Credits"
            ></b-form-input>
          </div>

          <div>
            <b-form-group label="Format" v-slot="{ ariaDescribedby }">
              <b-form-radio
                v-model="format"
                :aria-describedby="ariaDescribedby"
                name="some-radios3"
                value="vertical"
                >Oui</b-form-radio
              >
              <b-form-radio
                v-model="format"
                :aria-describedby="ariaDescribedby"
                name="some-radios3"
                value="horizontal"
                >Non</b-form-radio
              >
            </b-form-group>
          </div>

          <div id="tag">
            <label for="tags-basic">Type a new tag and press enter</label>
            <b-form-tags input-id="tags-basic" v-model="tags"></b-form-tags>
          </div>
        </div>
        <b-button type="submit" variant="primary">ENvoyer</b-button>
      </b-form>
    </div>

    <h1>Results</h1>

    <div name="photos">
      <div id="card" v-for="item in items" :key="item.id">
        <b-card
          title=""
          img-src="https://picsum.photos/600/300/?image=25"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20rem"
          class="mb-2"
        >
          <b-card-text>
            {{item.name}}
          </b-card-text>

          <!-- <b-button href="../views/Update.vue" variant="primary">update</b-button> -->
          <router-link :to="{ name: 'Update', params: { id: item.id }}">update</router-link>

        </b-card>
      </div>
    </div>
  </body>
</template>

<script>
import axios from "axios";

export default {
  name: "Search",
  data: () => {
    return {
      name: "",
      type: "",
      picture_product: "",
      picture_human: "",
      picture_institutional: "",
      tags: [],
      credits: "",
      format: "",
      items: []
    };
  },
  methods: {
    async onSubmit(event) {
      event.preventDefault();
      let formData = new FormData();
      formData.append("name", this.name);
      // formData.append("type", this.type);
      formData.append("picture_product", this.picture_product);
      // formData.append("picture_human", this.picture_human);
      // formData.append("picture_institutional", this.picture_institutional);
      // formData.append("tags", this.tags);
      // formData.append("credits", this.credits);
      // formData.append("format", this.format);

      console.log(...formData);
      let config = {
        method: "get",
        url: "/api/search",
        headers: { 'Content-Type': 'multipart/form-data' },
        data: formData
      };

      const response = await axios(config)
        .then(function (response) {
          return response;
        })
        .catch(function (error) {
          console.log(error);
        });

      this.items = response.data.results
    }
  }
};
</script>

<style>
h1 {
  margin-top: 2%;
}

/* #card {
  padding: 2%;
} */

#Forms {
  margin-top: 1%;
}
</style>
