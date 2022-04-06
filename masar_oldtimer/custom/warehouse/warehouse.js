frappe.ui.form.on("Warehouse", {
  warehouse_prefix: function (frm) {
    frm.set_value('warehouse_name', frm.doc.warehouse_prefix);
  },
  aisle: function (frm) {
  if (frm.doc.warehouse_name != '' && frm.doc.warehouse_name != null) {
    var wname = frm.doc.warehouse_name
     wname = wname + '-' + frm.doc.aisle;
    frm.set_value('warehouse_name', wname);
  }
  else {
    if (frm.doc.aisle != '' && frm.doc.aisle != null){
    frappe.msgprint("Please Fill Warehouse Prefix")
  }
}
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

// frappe.ui.form.on("Warehouse","parent_warehouse", function(frm){
// if (frm.parent_warehouse !=''){
// frm.doc.warehouse_prefix = frm.doc.parent_warehouse;
// frm.refresh_field('warehouse_prefix');
// }
// });
