"use strict"

let haushaltsbuch = {
     gesammtbilanz: {
          einnahmen: 0,
          ausgaben: 0,
          bilanz: 0,
     },
     neuer_eintrag: {
          titel: null,
          typ: null,
          betrag: null,
          datum: null
     },

     eintrag_erfassen() {
          this.neuer_eintrag.titel = prompt("Titel:")
          this.neuer_eintrag.typ = prompt("Typ Einnahme oder Ausgabe")
          this.neuer_eintrag.betrag = parseInt(prompt("betrag in Cent", "9999"))   // um nachkommerstellen zu vermeiden 
          this.neuer_eintrag.datum = prompt("gib das Datum ein jjjj.mm.tt:", "jjjj.mm.tt")          
     },
// we don`t use parametres becous we are in a objekt  
     eintrag_ausgeben() {
          console.log(`Tietel: ${this.neuer_eintrag.titel}
     Typ: ${this.neuer_eintrag.typ}
     Betrag: ${this.neuer_eintrag.betrag} ct 
     Datum: ${this.neuer_eintrag.datum}`)
     },

     eintrag_mit_gesammtbilanz_verrechnen() {
          if (this.neuer_eintrag.typ === "Einnahme") {
               this.gesammtbilanz.einnahmen += this.neuer_eintrag.betrag
               this.gesammtbilanz.bilanz += this.neuer_eintrag.betrag
           } 
           else if (this.neuer_eintrag.typ === "Ausgabe"){
               this.gesammtbilanz.ausgaben += this.neuer_eintrag.betrag
               this.gesammtbilanz.bilanz -= this.neuer_eintrag.betrag
           } else {
               console.log(`Der Typ "${this.neuer_eintrag.typ}" ist nicht bekannt.`)
           }
     
     },
     
     gesammtbilanz_ausgeben() {
          console.log(`Einnahmen: ${this.gesammtbilanz.einnahmen} ct
     Ausgaben: ${this.gesammtbilanz.ausgaben} ct
     Bilanz: ${this.gesammtbilanz.bilanz} ct
     Bilanz ist positiv; ${this.gesammtbilanz.bilanz >= 0}`)
     
     },

     eintrag_hinzufuegen() {
          this.eintrag_erfassen()
          this.eintrag_ausgeben(this.neuer_eintrag.titel, this.neuer_eintrag.typ, this.neuer_eintrag.betrag, this.neuer_eintrag.datum)
          this.eintrag_mit_gesammtbilanz_verrechnen(this.neuer_eintrag.typ, this.neuer_eintrag.betrag)
          this.gesammtbilanz_ausgeben(this.gesammtbilanz.einnahmen, this.gesammtbilanz.ausgaben, this.gesammtbilanz.bilanz)
     }


} 


haushaltsbuch.eintrag_hinzufuegen()
haushaltsbuch.eintrag_hinzufuegen()
haushaltsbuch.eintrag_hinzufuegen()
// // Gesammtbilnz 

// let positiv = bilanz >= 0
// console.log(`Bilanz: ${bilanz} ct
// Bilanz ist positiv; ${positiv}`)
 