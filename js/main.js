"use strict"

let  einnahmen = 0,
     ausgaben = 0,
     bilanz = 0,
     titel, 
     typ, 
     betrag, 
     datum 


const eintrag_erfassen = function(){
     titel = prompt("Titel:")
     typ = prompt("Typ Einnahme oder Ausgabe")
     betrag = parseInt(prompt("betrag in Cent", "9999"))   // um nachkommerstellen zu vermeiden 
     datum = prompt("gib das Datum ein jjjj.mm.tt:", "jjjj.mm.tt")
    

}

eintrag_erfassen()

const eintrag_ausgeben = function(titel, typ, betrag, datum) {
     console.log(`Tietel: ${titel}
               Typ: ${typ}
               Betrag: ${betrag} ct 
               Datum: ${datum}
               `)
}
eintrag_ausgeben(titel, typ, betrag, datum)

const eintrag_mit_gesammtbilanz_verrechnen = function(typ, bertag) {
     if (typ === "Einnahme") {
          einnahmen = einnahmen + betrag
          bilanz = bilanz + betrag
      } else if (typ === "Ausgabe"){
          ausgaben = ausgaben + betrag
          bilanz = bilanz - betrag
      } else {
          console.log(`Der Typ "${typ}" ist nicht bekannt.`)
      }

}
eintrag_mit_gesammtbilanz_verrechnen(typ, betrag)


const geammtbilanz_ausgeben = function(einnahmen, ausgaben, bilanz) {
     console.log(`Einnahmen: ${einnahmen} ct
     Ausgaben: ${ausgaben} ct
     Bilanz: ${bilanz} ct
     Bilanz ist positiv; ${bilanz >= 0}`
)
gesammtbilanz_ausgeben(einnahmen, ausgaben, bilanz)
} 

// // Gesammtbilnz 

// let positiv = bilanz >= 0
// console.log(`Bilanz: ${bilanz} ct
// Bilanz ist positiv; ${positiv}`)
 