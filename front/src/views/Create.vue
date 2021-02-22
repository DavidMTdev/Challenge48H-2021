<template>
  <body>
    <div name="button">
      <!-- <b-button variant="outline-danger">New</b-button> -->
      <router-link to="/">Back</router-link>
    </div>

    <h1>Update</h1>

    <div id="Forms">
      <b-form @submit="onSubmit" id="bform">
        <div>
          <div>
            <p>Nom de la photo</p>
            <b-form-input v-model="name" placeholder="Filename"></b-form-input>
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

          <div>
            <b-form-group
              label="Droits d’utilisation limités"
              v-slot="{ ariaDescribedby }"
            >
              <b-form-radio
                v-model="limited_utilisation_right"
                :aria-describedby="ariaDescribedby"
                name="some-radios"
                value="oui"
                >Oui</b-form-radio
              >
              <b-form-radio
                v-model="limited_utilisation_right"
                :aria-describedby="ariaDescribedby"
                name="some-radios"
                value="non"
                >Non</b-form-radio
              >
            </b-form-group>
          </div>

          <div>
            <p>Copyright</p>
            <b-form-input v-model="copyright" placeholder="complété si Droit d’utilisation limité = oui"></b-form-input>
          </div>
        </div>
        <div>
          <div>
            <label for="example-datepicker">Date de fin de droits d’utilisation</label>
            <b-form-datepicker id="example-datepicker" v-model="deadline_utilisation_right" class="mb-2"></b-form-datepicker>
          </div>
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
            <b-form-group label="format" v-slot="{ ariaDescribedby }">
              <b-form-radio
                v-model="format"
                :aria-describedby="ariaDescribedby"
                name="some-radios3"
                value="vertical"
                >vertical</b-form-radio
              >
              <b-form-radio
                v-model="format"
                :aria-describedby="ariaDescribedby"
                name="some-radios3"
                value="horizontal"
                >horizontal</b-form-radio
              >
            </b-form-group>
          </div>

          <div id="tag">
            <label for="tags-basic">Type a new tag and press enter</label>
            <b-form-tags input-id="tags-basic" v-model="tags"></b-form-tags>
          </div>

          <div>
            <!-- Styled -->
            <!-- <b-form-file
            v-model="file1"
            :state="Boolean(file1)"
            placeholder="Choose a file or drop it here..."
            drop-placeholder="Drop file here..."
            ></b-form-file>
            <div class="mt-3">Selected file: {{ file1 ? file1.name : '' }}</div> -->

            <!-- Plain mode -->
            <b-form-file
              @change="fileUpload"
              class="mt-3"
              plain
              multiple
            ></b-form-file>
            <div class="mt-3">Selected file: {{ files ? files.name : "" }}</div>
          </div>
        </div>
        <div name="button">
          <b-button type="submit" variant="outline-danger">Confirmer</b-button>
        </div>
      </b-form>
    </div>
  </body>
</template>

<script>
import axios from "axios";

export default {
  name: "Create",
  data() {
    return {
      name: "",
      type: "",
      picture_product: "",
      picture_human: "",
      picture_institutional: "",
      limited_utilisation_right: "",
      deadline_utilisation_right: "",
      copyright: "",
      tags: [],
      credits: "",
      format: "",
      files: FileList,
    };
  },
  methods: {
    fileUpload(event) {
      this.files = event.target.files;
    },
    onSubmit(event) {
      event.preventDefault();
      let formData = new FormData();
      formData.append("name", this.name);
      formData.append("type", this.type);
      formData.append("picture_product", this.picture_product);
      formData.append("picture_human", this.picture_human);
      formData.append("picture_institutional", this.picture_institutional);
      formData.append("limited_utilisation_right", this.limited_utilisation_right);
      formData.append("deadline_utilisation_right", this.deadline_utilisation_right);
      formData.append("copyright", this.copyright);
      formData.append("tags", this.tags);
      formData.append("credits", this.credits);
      formData.append("format", this.format);
      this.files.forEach(file => {
          formData.append("file", file, file.name);
      });

      console.log(...formData);
      let config = {
        method: "post",
        url: "/api/create",
        headers: { 'Content-Type': `multipart/form-data` },
        data: formData
      };

      const response = axios(config)
        .then(function (response) {
          return response;
        })
        .catch(function (error) {
          console.log(error);
        });

      console.log(response);
    },
  }
};
</script>

<style>
</style>