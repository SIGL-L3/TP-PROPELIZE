describe('Page Sign-in.vue', () => {

  beforeEach(() => {
    cy.visit('/sign-in')
  })

  it('✅ Affiche la page avec les champs username et password', () => {
    cy.get('input[placeholder="username"]').should('exist').and('have.attr', 'required')
    cy.get('input[placeholder="password"]').should('exist').and('have.attr', 'required')
    cy.contains('Sign in').should('exist')
  })

  it('✅ Permet de saisir username et password', () => {
    cy.get('input[placeholder="username"]').type('monUser').should('have.value', 'monUser')
    cy.get('input[placeholder="password"]').type('monPass').should('have.value', 'monPass')
  })

  it('🚀 Tente de se connecter avec succès et redirige vers /home', () => {
    // Intercept et mock la requête POST login
    cy.intercept('POST', 'http://127.0.0.1:8000/user/login/', {
      statusCode: 200,
      body: {
        access: 'fake-access-token',
        refresh: 'fake-refresh-token'
      }
    }).as('loginRequest')

    cy.get('input[placeholder="username"]').type('validUser')
    cy.get('input[placeholder="password"]').type('validPass')
    cy.get('button[type="submit"]').click()

    // Attend que la requête soit bien envoyée
    cy.wait('@loginRequest')

    // Vérifie que la redirection a eu lieu
    cy.url().should('include', '/home')
  })

  it('❌ Affiche un message d\'erreur en cas d\'échec de login', () => {
    // Intercept et mock un échec de login
    cy.intercept('POST', 'http://127.0.0.1:8000/user/login/', {
      statusCode: 401,
      body: {
        detail: 'Invalid credentials'
      }
    }).as('loginRequest')

    cy.get('input[placeholder="username"]').type('wrongUser')
    cy.get('input[placeholder="password"]').type('wrongPass')
    cy.get('button[type="submit"]').click()

    // Attend la requête
    cy.wait('@loginRequest')

    // Vérifie l'affichage du message d'erreur
    cy.get('p.error.visible').should('be.visible').and('contain.text', 'Invalid password or username')

    // Vérifie qu'on reste sur la page de connexion
    cy.url().should('include', '/sign-in')
  })

  it('🔗 Clique sur Sign up redirige vers /sign-up', () => {
    cy.get('span').contains('Sign up').click()
    cy.url().should('include', '/sign-up')
  })

})
