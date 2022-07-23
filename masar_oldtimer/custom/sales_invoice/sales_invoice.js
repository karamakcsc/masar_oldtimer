//
//
//
// frappe.ui.form.on('Sales Invoice', {
//   refresh(frm) {
//     frm.fields_dict["items"].grid.add_custom_button(__('Search for Warehouse'),
//       function() {
//         var current_doc = $('.data-row.editable-row').parent().attr("data-name");
//         var row = locals["Sales Invoice Item"][current_doc];
//         let query_args = {
//             //Backend method that get's called and returns the Categories
//             query: "masar_oldtimer.custom.sales_invoice.sales_invoice.get_bin_qry",
//             filters: {'item_code': row.item_code}
//         }
//         var d = new frappe.ui.form.MultiSelectDialog({
//             doctype: "Bin",
//             target: this.cur_frm,
//             setters: {
//               warehouse: '',
//               actual_qty: ''
//                         },
//             add_filters_group: 1,
//             date_field: "item_code",
//             columns: ["item_code","warehouse","actual_qty"],
//             get_query() {
//                return query_args;
//            },
//             primary_action_label: "Get Item",
// 						action(selected_bins) {
// 							frappe.call({
// 								method: "masar_oldtimer.custom.sales_invoice.sales_invoice.insert_selected_bins",
// 								args: {
// 									selected_bins: selected_bins
// 								},
// 								callback: function(r) {
// 									$.each(r.message, function(i, d) {
// 										// var row = frappe.model.add_child(frm.doc, "Sales Invoice Item", "items");
// 										row.warehouse = d.warehouse;
// 										refresh_field("items");
// 									});
// 								}
// 							});
// 							d.dialog.hide();
// 						}
//         });
//     }
//   )
// 	frm.fields_dict["items"].grid.grid_buttons.find('.btn-custom').removeClass('btn-default').addClass('btn-primary');
// }
//
// });
