function updateNotification(statuses) {
  console.log(statuses);
  for (let i = 0; i < statuses.length; i++) {
    alert("Order status changed to " + statuses[i]);
  }
}
