<template>
  <body>
    <div>
      <router-link to="/" id="button" ><b-icon-arrow-left></b-icon-arrow-left></router-link>
    </div>

    <div class="mt-5">
     <h1>Update image</h1>
    </div>

    <div id= "Forms">
      <b-form inline id="bform" @submit="onSubmit">
        <div id="form1">
          <div id="input">
            <p>Nom de la photo</p>
            <b-form-input v-model="name" placeholder="Filename"></b-form-input>
          </div>

          <div id="input">
            <p>Type d'image</p>
            <b-form-input v-model="type" placeholder="Image type"></b-form-input>
          </div>
      
          <div id="input">
            <b-form-group label="Photo avec produit" v-slot="{ ariaDescribedby }">
              <b-form-radio v-model="picture_product" :aria-describedby="ariaDescribedby" name="some-radios" value="oui">Oui</b-form-radio>
              <b-form-radio v-model="picture_product" :aria-describedby="ariaDescribedby" name="some-radios" value="non">Non</b-form-radio>
            </b-form-group>

          </div>

          <div id="input">
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

          <div id="input">
            <p>Copyright</p>
            <b-form-input v-model="copyright" placeholder="complété si Droit d’utilisation limité = oui"></b-form-input>
          </div>

        </div>
        <div id="form1">

          <div id="input">
            <label for="example-datepicker">Date de fin de droits d’utilisation</label>
            <b-form-datepicker id="example-datepicker" v-model="deadline_utilisation_right" class="mb-2"></b-form-datepicker>
          </div>

          <div id="input">
            <b-form-group label="Photo avec Humain" v-slot="{ ariaDescribedby }">
                <b-form-radio v-model="picture_human" :aria-describedby="ariaDescribedby" name="some-radios1" value="oui">Oui</b-form-radio>
                <b-form-radio v-model="picture_human" :aria-describedby="ariaDescribedby" name="some-radios1" value="non">Non</b-form-radio>
            </b-form-group>
          </div>

          <div id="input">
            <b-form-group label="Photo institutionnelle" v-slot="{ ariaDescribedby }">
              <b-form-radio v-model="picture_institutional" :aria-describedby="ariaDescribedby" name="some-radios2" value="oui">Oui</b-form-radio>
              <b-form-radio v-model="picture_institutional" :aria-describedby="ariaDescribedby" name="some-radios2" value="non">Non</b-form-radio>
            </b-form-group>

          </div>

          

        </div>
        <div id="form1">
          
          <div id="input">
            <p>Credits de la photo</p>
            <b-form-input v-model="credits" placeholder="Credits"></b-form-input>
          </div>

          <div id="input">
            <b-form-group label="format" v-slot="{ ariaDescribedby }">
              <b-form-radio v-model="format" :aria-describedby="ariaDescribedby" name="some-radios3" value="vertical">vertical</b-form-radio>
              <b-form-radio v-model="format" :aria-describedby="ariaDescribedby" name="some-radios3" value="horizontal">horizontal</b-form-radio>
            </b-form-group>

          </div>

          <div id="input">
            <label for="tags-basic">Enter tags you want</label>
            <b-form-tags input-id="tags-basic" v-model="tags"></b-form-tags>
            <!-- <p class="mt-2">Value: {{ value }}</p> -->
          </div>

          <div id="input">
            <!-- Styled -->
            <!-- <b-form-file
            v-model="file1"
            :state="Boolean(file1)"
            placeholder="Choose a file or drop it here..."
            drop-placeholder="Drop file here..."
            multiple
            ></b-form-file>
            <div class="mt-3">Selected file: {{ file1 ? file1.name : '' }}</div>-->

            <!-- Plain mode -->
            <b-form-file v-model="file" class="mt-3" plain></b-form-file>
            <div class="mt-3">Selected file: {{ file ? file.name : '' }}</div>
          </div> 

        </div>
        <div name="button" style="padding-left: 40%;">
          <b-button type="submit" variant="outline-danger">Confirmer</b-button>
        </div>
      </b-form>
    </div>   

  </body>
</template>

<script>
import axios from "axios";

export default {
  name: "Update",
  data: function () {
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
      file: "",
    };
  },
  mounted: function () {
    this.getSearchById();
  },
  methods: {
    async getSearchById() {
      let config = {
        method: "get",
        url: `/api/search/${this.$route.params.id}`
      };

      const response = await axios(config)
        .then(function (response) {
          return response;
        })
        .catch(function (error) {
          console.log(error);
        });

      console.log(response);

      this.name = response.data.result.name
      this.type = response.data.result.type
      this.picture_product = response.data.result.picture_product
      this.picture_human = response.data.result.picture_human
      this.picture_institutional = response.data.result.picture_institutional
      this.limited_utilisation_right = response.data.result.limited_utilisation_right
      this.deadline_utilisation_right = response.data.result.deadline_utilisation_right
      this.copyright = response.data.result.copyright
      this.tags = response.data.result.tags
      this.credits = response.data.result.credits
      this.format = response.data.result.format
    },
    fileUpload(event) {
      this.file = event.target.files[0];
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
      console.log(this.file);

      if (this.file) {
        formData.append("file", this.file, this.file.name);
      }


      console.log(...formData);
      let config = {
        method: "post",
        url: `/api/update/${this.$route.params.id}`,
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

#form1{
  padding: 5%;
  height: 100%;
}

#input{
  margin: 10%;
  max-width: 300px;
}

#Forms{
  margin-top: 1%;
}

</style>