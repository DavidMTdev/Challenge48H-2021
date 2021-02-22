<template>
  <body>
    
    <div name="button">
      <b-button variant="outline-danger">New</b-button>
    </div>
    
    <h1>Your request</h1>

    <div id= "Forms">
      <b-form inline id="bform">
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
        </div>
      </b-form>
    </div>   

    <h1>Results</h1>

    <div name="photos">
      <div id= "card">
        <b-card
          title="CardTitle"
          img-src="https://picsum.photos/600/300/?image=25"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20rem;"
          class="mb-2"
        >
        <b-card-text>
          Some quick example text to build on the card title and make up the bulk of the card's content.
        </b-card-text>

        <b-button href="../views/Update.vue" variant="primary">test</b-button>
        </b-card>
      
      </div>
    </div>
  </body>
  
</template>

<script>
export default {
  name: "Search",
  data: function () {
    return {
      value: ['pomme', 'poire']
    };
  },
};
</script>

<style>

h1{
  margin-top: 2%;
}

#card{
  padding: 2%;
}

#Forms{
  margin-top: 1%;

}

</style>
