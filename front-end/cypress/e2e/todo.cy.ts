/// <reference types="cypress" />

describe('Web app end-tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:1234/')
  })

  it('contains some text', () => {
    cy.get('.card button').contains("count is ")
  })
})
