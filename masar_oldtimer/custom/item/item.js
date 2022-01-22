

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
