// Filter From Account List When Based on Transaction Type

// frappe.ui.form.on("Item", {
//   first_category: function(frm) {
//     if (frm.doc.first_category != '') {
//       frm.set_query("second_category", function() {
//         return {
//           query: "masar_oldtimer.custom.item.item.second_category_query",
//           filters: {'first_category': frm.doc.first_category,
//                     'item_code': frm.doc.item_code}
//         }
//       });
//     }
//     frm.set_value("second_category",'')
//     frm.set_value("third_category",'')
//   },
//   second_category: function(frm) {
//     if (frm.doc.first_category != '' && frm.doc.second_category != '') {
//       frm.set_query("third_category", function() {
//         return {
//           query: "masar_oldtimer.custom.item.item.third_category_query",
//           filters: {'first_category': frm.doc.first_category,
//                     'second_category': frm.doc.second_category}
//         }
//       });
//     }
//   frm.set_value("third_category",'')
//   }
//
// });

// First Category
frappe.ui.form.on("Item", {
  add_first_category: function(frm){
    var f = new frappe.ui.form.MultiSelectDialog({
      doctype: "Item First Category",
      target: me.frm,
      setters: {
        first_category: ""
      },
      date_field: "first_category",
      primary_action_label: "Get Category",
      action(selected_categories) {
        frappe.call({
          method: "masar_oldtimer.custom.item.item.insert_selected_first_category",
          args: {
            selected_categories: selected_categories
          },
          callback: function(r) {
            $.each(r.message, function(i, d) {
              var row = frappe.model.add_child(cur_frm.doc, "Item First Category Value", "first_category");
              row.first_category = d.first_category;
              refresh_field("first_category");
            });
          }
        });
        f.dialog.hide();
      }
    })
	}
});



//Second Category
frappe.ui.form.on("Item", {
  add_second_category: function(frm){

    if(frm.doc.first_category.length == 0){
      frappe.msgprint("Please fill first categories!")
      return
    }

  var categories = new Array();
  var first_categories = frm.doc.first_category;

 	first_categories.forEach(function(entry) {
 		if (entry.first_category != null) {
 	     	categories.push(entry.first_category);
  	}
 });

    let query_args = {
        //Backend method that get's called and returns the Categories
        query: "masar_oldtimer.custom.item.item.second_category_query",
        filters: {'item_code': frm.doc.item_code,'categories': categories}
    }
    var s = new frappe.ui.form.MultiSelectDialog({
      doctype: "Item Second Category",
      target: me.frm,
      setters: {
        first_category: ""
      },
      add_filters_group: 1,
      columns: ["name", "first_category"],
      get_query() {
         return query_args;
     },
      primary_action_label: "Get Category",
      action(selected_categories) {
        frappe.call({
          method: "masar_oldtimer.custom.item.item.insert_selected_second_category",
          args: {
            selected_categories: selected_categories
          },
          callback: function(r) {
            $.each(r.message, function(i, d) {
              var row = frappe.model.add_child(cur_frm.doc, "Item Second Category Value", "second_category");
              row.second_category = d.second_category;
              refresh_field("second_category");
            });
          }
        });
        s.dialog.hide();
      }
    })
	}
});



// Third Category
frappe.ui.form.on("Item", {
  add_third_category: function(frm){
    if(frm.doc.second_category.length == 0){
      frappe.msgprint("Please fill second categories!")
      return
    }
    var categories = new Array();
    var second_categories = frm.doc.second_category;

    second_categories.forEach(function(entry) {
      if (entry.second_category != null) {
          categories.push(entry.second_category);
      }
    });

    let query_args = {
        //Backend method that get's called and returns the Categories
        query: "masar_oldtimer.custom.item.item.third_category_query",
        filters: {'item_code': frm.doc.item_code,'categories': categories}
    }

    var t = new frappe.ui.form.MultiSelectDialog({
      doctype: "Item Third Category",
      target: me.frm,
      setters: {
        second_category: "",
        first_category: ""
      },
      add_filters_group: 1,
      columns: ["name", "second_category","first_category"],
      get_query() {
         return query_args;
     },
      primary_action_label: "Get Category",
      action(selected_categories) {
        //frappe.msgprint("HI")
        frappe.call({
          method: "masar_oldtimer.custom.item.item.insert_selected_third_category",
          args: {
            selected_categories: selected_categories
          },
          callback: function(r) {
            $.each(r.message, function(i, d) {
              var row = frappe.model.add_child(cur_frm.doc, "Item Third Category Value", "third_category");
              row.third_category = d.third_category;
              refresh_field("third_category");
            });
          }
        });
        t.dialog.hide();
      }
    })
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
