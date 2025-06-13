describe('Tests de la page Home.vue', () => {

  it('1️⃣ Charge les véhicules depuis l’API', () => {
    // ton test qui passe déjà
  })

  it('2️⃣ Crée un nouveau véhicule', () => {
    cy.get('input[placeholder="registration number"]').type('1234ABC')
    cy.get('input[placeholder="make"]').type('Toyota')
    cy.get('input[placeholder="model"]').type('Corolla')
    cy.get('input[placeholder="year"]').type('2023')
    cy.get('input[placeholder="rental price"]').type('123000')  // corrigé ici
    cy.get('button').contains('+').click()

    cy.wait(1000) // attendre que la liste soit mise à jour

    cy.contains('Toyota', { matchCase: false }).should('exist')
  })

  it('3️⃣ Filtre les véhicules par numéro d\'immatriculation', () => {
    cy.get('input[placeholder="registration number"]').clear().type('1234ABC')  // corrigé ici
    cy.wait(500)
    cy.contains('1234ABC').should('exist')
  })

  it('4️⃣ Filtre les véhicules par prix maximum', () => {
    cy.get('input[placeholder="max price"]').clear().type('10000')
    cy.get('form').submit()  // ou cy.get('i.bx-search').click()

    cy.wait(1000)

    // Exemple si le composant Car expose le prix avec classe 'vehicule-price'
    cy.get('.vehicule-price').each(($el) => {
      const priceText = $el.text()
      const price = parseInt(priceText.replace(/\D/g, ''))
      expect(price).to.be.lte(10000)
    })
  })

  it('5️⃣ Permet de se déconnecter', () => {
    // ton test qui passe déjà
  })

})
