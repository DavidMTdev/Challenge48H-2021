<template>
  <body>
    
    <div name="button">
      <router-link to="/" id="button"><b-icon-arrow-left></b-icon-arrow-left></router-link>
    </div>
    
    <h1>Update</h1>

    <div id= "Forms">
      <b-form id="bform">
        <div>
          <div>
            <p>Nom de la photo</p>
            <b-form-input v-model="name" placeholder="Filename"></b-form-input>
          </div>

          <div>
            <p>Type d'image</p>
            <b-form-input v-model="type" placeholder="Image type"></b-form-input>
          </div>
      
          <div>
            <b-form-group label="Photo avec produit" v-slot="{ ariaDescribedby }">
              <b-form-radio v-model="picture_product" :aria-describedby="ariaDescribedby" name="some-radios" value="oui">Oui</b-form-radio>
              <b-form-radio v-model="picture_product" :aria-describedby="ariaDescribedby" name="some-radios" value="non">Non</b-form-radio>
            </b-form-group>

          </div>
        </div>
        <div>
          <div>
            <b-form-group label="Photo avec Humain" v-slot="{ ariaDescribedby }">
                <b-form-radio v-model="picture_human" :aria-describedby="ariaDescribedby" name="some-radios1" value="oui">Oui</b-form-radio>
                <b-form-radio v-model="picture_human" :aria-describedby="ariaDescribedby" name="some-radios1" value="non">Non</b-form-radio>
            </b-form-group>
          </div>

          <div>
            <b-form-group label="Photo institutionnelle" v-slot="{ ariaDescribedby }">
              <b-form-radio v-model="picture_institutional" :aria-describedby="ariaDescribedby" name="some-radios2" value="oui">Oui</b-form-radio>
              <b-form-radio v-model="picture_institutional" :aria-describedby="ariaDescribedby" name="some-radios2" value="non">Non</b-form-radio>
            </b-form-group>

          </div>
        </div>
        <div>
          <div>
            <p>Credits de la photo</p>
            <b-form-input v-model="credits" placeholder="Credits"></b-form-input>
          </div>

          <div>
            <b-form-group label="format" v-slot="{ ariaDescribedby }">
              <b-form-radio v-model="format" :aria-describedby="ariaDescribedby" name="some-radios3" value="vertical">vertical</b-form-radio>
              <b-form-radio v-model="format" :aria-describedby="ariaDescribedby" name="some-radios3" value="horizontal">horizontal</b-form-radio>
            </b-form-group>

          </div>

          <div id= "tag">
            <label for="tags-basic">Type a new tag and press enter</label>
            <b-form-tags input-id="tags-basic" v-model="tags"></b-form-tags>
            <p class="mt-2">Value: {{ value }}</p>
          </div>

          <div>
            <!-- Styled -->
            <b-form-file
            v-model="file1"
            :state="Boolean(file1)"
            placeholder="Choose a file or drop it here..."
            drop-placeholder="Drop file here..."
            ></b-form-file>
            <div class="mt-3">Selected file: {{ file1 ? file1.name : '' }}</div>

            <!-- Plain mode -->
            <b-form-file v-model="file2" class="mt-3" plain multiple></b-form-file>
            <div class="mt-3">Selected file: {{ file2 ? file2.name : '' }}</div>
          </div>

        </div>
      </b-form>
    </div>   

    <div name="button">
      <b-button variant="outline-danger">Confirmer</b-button>
    </div>

  </body>
</template>

<script>
export default {
  name: "Update",
  data: function () {
    return {};
  },
};
</script>

<style>
</style>