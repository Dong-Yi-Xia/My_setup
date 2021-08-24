from typing import Any

from django.db.backends.base.features import BaseDatabaseFeatures as BaseDatabaseFeatures

class DatabaseFeatures(BaseDatabaseFeatures):
    empty_fetchmany_value: Any = ...
    allows_group_by_pk: bool = ...
    related_fields_match_type: bool = ...
    allow_sliced_subqueries_with_in: bool = ...
    has_select_for_update: bool = ...
    supports_forward_references: bool = ...
    supports_regex_backreferencing: bool = ...
    supports_date_lookup_using_string: bool = ...
    can_introspect_autofield: bool = ...
    can_introspect_binary_field: bool = ...
    can_introspect_duration_field: bool = ...
    can_introspect_small_integer_field: bool = ...
    can_introspect_positive_integer_field: bool = ...
    introspected_boolean_field_type: str = ...
    supports_index_column_ordering: bool = ...
    supports_timezones: bool = ...
    requires_explicit_null_ordering_when_grouping: bool = ...
    allows_auto_pk_0: bool = ...
    can_release_savepoints: bool = ...
    atomic_transactions: bool = ...
    can_clone_databases: bool = ...
    supports_temporal_subtraction: bool = ...
    supports_select_intersection: bool = ...
    supports_select_difference: bool = ...
    supports_slicing_ordering_in_compound: bool = ...
    supports_index_on_text_field: bool = ...
    has_case_insensitive_like: bool = ...
    create_test_procedure_without_params_sql: str = ...
    create_test_procedure_with_int_param_sql: str = ...
    db_functions_convert_bytes_to_str: bool = ...
    supports_partial_indexes: bool = ...
    supports_order_by_nulls_modifier: bool = ...
    order_by_nulls_first: bool = ...
    def update_can_self_select(self): ...
    def can_introspect_foreign_keys(self): ...
    def can_return_columns_from_insert(self): ...
    can_return_rows_from_bulk_insert: Any = ...
    def has_zoneinfo_database(self): ...
    def is_sql_auto_is_null_enabled(self): ...
    def supports_over_clause(self): ...
    supports_frame_range_fixed_distance: Any = ...
    def supports_column_check_constraints(self): ...
    supports_table_check_constraints: Any = ...
    def can_introspect_check_constraints(self): ...
    def has_select_for_update_skip_locked(self): ...
    def has_select_for_update_nowait(self): ...
    def needs_explain_extended(self): ...
    def supports_explain_analyze(self): ...
    def supported_explain_formats(self): ...
    def supports_transactions(self): ...
    def ignores_table_name_case(self): ...
    def supports_default_in_lead_lag(self): ...
    def supports_json_field(self): ...
    def can_introspect_json_field(self): ...