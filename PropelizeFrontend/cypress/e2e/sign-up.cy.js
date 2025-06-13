describe('Page Sign-up.vue', () => {

  beforeEach(() => {
    cy.visit('/sign-up')  // adapte selon ta route réelle
  })

  it('✅ Affiche les champs username et password', () => {
    cy.get('input[placeholder="username"]').should('exist').and('have.attr', 'required')
    cy.get('input[placeholder="password"]').should('exist').and('have.attr', 'required')
    cy.contains('Sign up').should('exist')
  })

  it('✅ Permet de saisir username et password', () => {
    cy.get('input[placeholder="username"]').type('nouveauUser').should('have.value', 'nouveauUser')
    cy.get('input[placeholder="password"]').type('motdepasse123').should('have.value', 'motdepasse123')
  })

  it('🚀 Soumission réussie redirige vers /sign-in', () => {
    // Stub l'appel axios POST pour simuler succès
    cy.intercept('POST', 'http://127.0.0.1:8000/user/create/', {
      statusCode: 201,
      body: { id: 1, name: 'nouveauUser' }
    }).as('registerUser')

    cy.get('input[placeholder="username"]').type('nouveauUser')
    cy.get('input[placeholder="password"]').type('motdepasse123')
    cy.get('button').contains('Sign up').click()

    cy.wait('@registerUser')
    cy.url().should('include', '/sign-in')
  })

  it('❌ Affiche erreur si username déjà pris (400)', () => {
    // Stub axios POST pour simuler erreur 400
    cy.intercept('POST', 'http://127.0.0.1:8000/user/create/', {
      statusCode: 400,
      body: { error: 'username already taken' }
    }).as('registerUserFail')

    cy.get('input[placeholder="username"]').type('userExistant')
    cy.get('input[placeholder="password"]').type('motdepasse')
    cy.get('button').contains('Sign up').click()

    cy.wait('@registerUserFail')
    cy.get('#error').should('be.visible').and('contain.text', 'username already take')
    cy.url().should('include', '/sign-up')
  })

  it('🔗 Clique sur Sign in redirige vers /sign-in', () => {
    cy.get('span').contains('Sign in').click()
    cy.url().should('include', '/sign-in')
  })

})
