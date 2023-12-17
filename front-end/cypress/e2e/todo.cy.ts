/// <reference types="cypress" />

describe('Web app end-tests', () => {
  beforeEach(() => {
    cy.visit(Cypress.config('baseUrl'))
  })

  it('contains some text', () => {
    cy.get('h1').contains("Generate QR Code")
  })
})
