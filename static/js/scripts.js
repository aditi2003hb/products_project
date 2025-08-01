// Confirm before toggling a user's status
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll('a[href*="/users/toggle/"]').forEach(link => {
    link.addEventListener("click", event => {
      const action = link.textContent.trim();
      if (!confirm(`Are you sure you want to ${action.toLowerCase()} this user?`)) {
        event.preventDefault();
      }
    });
  });

  // Prevent negative credit/debit
  const txForm = document.querySelector('form[action="/transactions/add"]');
  if (txForm) {
    txForm.addEventListener("submit", event => {
      const credit = parseFloat(txForm.credit.value) || 0;
      const debit  = parseFloat(txForm.debit.value)  || 0;
      if (credit < 0 || debit < 0) {
        alert("Credit and debit must be non-negative numbers.");
        event.preventDefault();
      }
    });
  }
});
