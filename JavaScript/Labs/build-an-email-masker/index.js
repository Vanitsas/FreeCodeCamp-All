function maskEmail(email) {
  const atIndex = email.indexOf("@");

  const username = email.slice(0, atIndex);
  const domain = email.slice(atIndex);

  if (username.length <= 2) {
    return username[0] + "*".repeat(username.length - 1) + domain;
  }

  const firstChar = username[0];
  const lastChar = username[username.length - 1];

  const maskedMiddle = "*".repeat(username.length - 2);

  return firstChar + maskedMiddle + lastChar + domain;
}

// dışarıda email değişkeni
const email = "apple.pie@example.com";

// çağır ve yazdır
console.log(maskEmail(email));