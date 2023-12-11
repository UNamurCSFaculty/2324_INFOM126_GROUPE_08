/// <reference types="cypress" />

describe('Web app end-tests', () => {
  beforeEach(() => {
    cy.visit(Cypress.config('baseUrl'))
  })

  it('contains some text', () => {
    cy.get('.card button').contains("count is ")
  })
})
