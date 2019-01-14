const repeatedString = (s, n) => {
    if (s === 'a'){
      return n;
    }
  
    const max_amount = Math.floor(n / s.length);
    
    let count = 0;
    for (let x of s){
      if (x === 'a'){
        count += 1
      }
    }
  
    if (n % s.length === 0){
      return count * max_amount; 
    } else {
      count = count * max_amount; 
      const index = n % s.length; 
      const new_s = s.slice(0, index)
      console.log(new_s)
      for (let y of new_s){
        if (y === 'a'){
          count += 1
        }
      }
  
      return count; 
    }
  
  }
  
  
  console.log(repeatedString("epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq", 549382313570))
  
  console.log(repeatedString("kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm", 736778906400))