let count = 0;

function cardCounter(card) {
  // 2-6 arası +1
  if (card >= 2 && card <= 6) {
    count++;
  }
  // 7-9 arası değişmez
  else if (card >= 7 && card <= 9) {
    count += 0;
  }
  // 10, J, Q, K, A -1
  else if (
    card === 10 ||
    card === "J" ||
    card === "Q" ||
    card === "K" ||
    card === "A"
  ) {
    count--;
  }

  // karar
  if (count > 0) {
    return count + " Bet";
  } else {
    return count + " Hold";
  }
}

