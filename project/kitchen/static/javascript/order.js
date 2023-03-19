function updateOrderStatus(orderID) {
    cookieData = "orderID=" + orderID + "; ";
    expiryDate = new Date();
    expiryDate.setTime(expiryDate.getTime() + (5 * 1000));
    cookieExpiry = "expires=" + expiryDate.toUTCString() + "; ";
    
    document.cookie = cookieData + cookieExpiry + "path=/";

    window.location.href = "http://127.0.0.1:8000/kitchen/";
}