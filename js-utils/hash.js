const jsonString = process.argv[2];
const crypto = require('node:crypto');
const parsedJson = JSON.parse(jsonString);

async function hash(text) {
    const encoder = new TextEncoder();
    const data = encoder.encode(text);
    const hashBuffer = await crypto.subtle.digest("SHA-256", data);

    const hashArray = Array.from(new Uint8Array(hashBuffer));

    
    const hashHex = hashArray.map((b) => b.toString(16).padStart(2, "0")).join("");
    console.log(hashHex);
    
    return hashHex;
  }


const result = JSON.stringify(parsedJson);
final_res = hash(result);