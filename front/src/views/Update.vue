<template>
  <body>
    
    <div name="button">
      <b-button variant="outline-danger">New</b-button>
    </div>
    
    <h1>New picture</h1>

    <div id= "Forms">
      <b-form id="bform">
        <div>
          <div>
            <p>Nom de la photo</p>
            <b-form-input v-model="text" placeholder="Filename"></b-form-input>
          </div>

          <div>
            <p>Type d'image</p>
            <b-form-input v-model="text" placeholder="Image type"></b-form-input>
          </div>
      
          <div>
            <b-form-group label="Photo avec produit" v-slot="{ ariaDescribedby }">
              <b-form-radio v-model="selected" :aria-describedby="ariaDescribedby" name="some-radios" value="A">Oui</b-form-radio>
              <b-form-radio v-model="selected" :aria-describedby="ariaDescribedby" name="some-radios" value="B">Non</b-form-radio>
            </b-form-group>

          </div>
        </div>
        <div>
          <div>
            <b-form-group label="Photo avec Humain" v-slot="{ ariaDescribedby }">
                <b-form-radio v-model="selected1" :aria-describedby="ariaDescribedby" name="some-radios1" value="A">Oui</b-form-radio>
                <b-form-radio v-model="selected1" :aria-describedby="ariaDescribedby" name="some-radios1" value="B">Non</b-form-radio>
            </b-form-group>
          </div>

          <div>
            <b-form-group label="Photo institutionnelle" v-slot="{ ariaDescribedby }">
              <b-form-radio v-model="selected2" :aria-describedby="ariaDescribedby" name="some-radios2" value="A">Oui</b-form-radio>
              <b-form-radio v-model="selected2" :aria-describedby="ariaDescribedby" name="some-radios2" value="B">Non</b-form-radio>
            </b-form-group>

          </div>
        </div>
        <div>
          <div>
            <p>Credits de la photo</p>
            <b-form-input v-model="text" placeholder="Credits"></b-form-input>
          </div>

          <div>
            <b-form-group label="Format" v-slot="{ ariaDescribedby }">
              <b-form-radio v-model="selected4" :aria-describedby="ariaDescribedby" name="some-radios3" value="A">Oui</b-form-radio>
              <b-form-radio v-model="selected4" :aria-describedby="ariaDescribedby" name="some-radios3" value="B">Non</b-form-radio>
            </b-form-group>

          </div>

          <div id= "tag">
            <label for="tags-basic">Type a new tag and press enter</label>
            <b-form-tags input-id="tags-basic" v-model="value"></b-form-tags>
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