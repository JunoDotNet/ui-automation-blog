describe('Static Blog Test', () => {
  it('loads local test page and finds button', () => {
    cy.visit('http://localhost:8080');
    cy.contains('Tech Tutorials').should('be.visible');
  });
});
