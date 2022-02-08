frappe.ui.form.on("Warehouse", {
  aisle: function (frm) {
    frm.set_value('warehouse_name', frm.doc.aisle);
  },
  unit: function (frm) {
  if (frm.doc.warehouse_name != '' && frm.doc.warehouse_name != null) {
    var wname = frm.doc.warehouse_name
     wname = wname + '-' + frm.doc.unit;
    frm.set_value('warehouse_name', wname);
  }
  else {
    if (frm.doc.unit != '' && frm.doc.unit != null){
    frappe.msgprint("Please fill aisle")
  }
}
},
  shelf: function (frm) {
    if (frm.doc.warehouse_name != '' && frm.doc.warehouse_name != null) {
      var wname = frm.doc.warehouse_name
       wname = wname + '-' + frm.doc.shelf;
      frm.set_value('warehouse_name', wname);
    }
    else {
      if (frm.doc.shelf != '' && frm.doc.shelf != null){
      frappe.msgprint("Please fill unit")
    }
    }
  },
  bin: function (frm) {
    if (frm.doc.warehouse_name != '' && frm.doc.warehouse_name != null) {
      var wname = frm.doc.warehouse_name
       wname = wname + '-' + frm.doc.bin;
      frm.set_value('warehouse_name', wname);
    }
    else {
      if (frm.doc.bin != '' && frm.doc.bin != null){
      frappe.msgprint("Please fill shelf")
    }
    }
  }
});
