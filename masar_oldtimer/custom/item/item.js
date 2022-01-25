

// Filter From Account List When Based on Transaction Type

frappe.ui.form.on("Item", {
  item_first_category: function(frm) {
    if (frm.doc.item_first_category != '') {
      frm.set_query("item_second_category", function() {
        return {
          query: "masar_oldtimer.custom.item.item.second_category_query",
          filters: {'first_category': frm.doc.item_first_category}
        }
      });
    }
    frm.set_value("item_second_category",'')
    frm.set_value("item_third_category",'')
  },
  item_second_category: function(frm) {
    if (frm.doc.item_first_category != '' && frm.doc.item_second_category != '') {
      frm.set_query("item_third_category", function() {
        return {
          query: "masar_oldtimer.custom.item.item.third_category_query",
          filters: {'first_category': frm.doc.item_first_category,
                    'second_category': frm.doc.item_second_category}
        }
      });
    }
  frm.set_value("item_third_category",'')
  }

});


frappe.ui.form.on("Item", {
	item_length: function(frm){
  calculate_total(frm);
	},
	item_width: function(frm){
		calculate_total(frm);
	},
  item_height: function(frm){
  calculate_total(frm);
  },
  volumetric_factor: function(frm){
  calculate_total(frm);
  }
});

var calculate_total = function(frm) {
  var doc = frm.doc
  if (doc.volumetric_factor != 0) {
    frm.set_value("volumetric_weight",(doc.item_length * doc.item_width * doc.item_height)/doc.volumetric_factor)
	    }
  else {
      frm.set_value("volumetric_weight",0);
  }
}
