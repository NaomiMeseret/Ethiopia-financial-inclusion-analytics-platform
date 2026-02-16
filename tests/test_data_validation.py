"""
Data validation tests for Ethiopia Financial Inclusion Forecasting System
"""
import pandas as pd
import pytest
import sys
import os

# Add src directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

class TestDataValidation:
    """Test suite for data validation"""
    
    @pytest.fixture
    def enriched_data(self):
        """Load enriched dataset for testing"""
        data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed', 'ethiopia_fi_enriched_data.csv')
        return pd.read_csv(data_path)
    
    @pytest.fixture
    def reference_codes(self):
        """Load reference codes for validation"""
        ref_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'reference_codes.csv')
        return pd.read_csv(ref_path)
    
    def test_dataset_structure(self, enriched_data):
        """Test that dataset has required columns"""
        required_columns = [
            'record_id', 'record_type', 'pillar', 'indicator', 'indicator_code',
            'value_numeric', 'value_text', 'observation_date', 'source_name', 'source_url',
            'confidence', 'original_text', 'notes', 'collected_by', 'collection_date',
            'parent_id', 'related_indicator', 'impact_direction', 'impact_magnitude', 
            'lag_months', 'evidence_basis'
        ]
        
        for col in required_columns:
            assert col in enriched_data.columns, f"Missing required column: {col}"
    
    def test_record_types(self, enriched_data, reference_codes):
        """Test that all record_types are valid"""
        valid_record_types = reference_codes[reference_codes['field'] == 'record_type']['code'].tolist()
        actual_record_types = enriched_data['record_type'].unique()
        
        for record_type in actual_record_types:
            assert record_type in valid_record_types, f"Invalid record_type: {record_type}"
    
    def test_pillar_values(self, enriched_data, reference_codes):
        """Test that pillar values are valid"""
        valid_pillars = reference_codes[reference_codes['field'] == 'pillar']['code'].tolist()
        valid_pillars.append('')  # Empty string is valid for events
        
        # Only check non-empty pillars
        non_empty_pillars = enriched_data[enriched_data['pillar'] != '']['pillar'].unique()
        
        for pillar in non_empty_pillars:
            assert pillar in valid_pillars, f"Invalid pillar: {pillar}"
    
    def test_confidence_levels(self, enriched_data, reference_codes):
        """Test that confidence levels are valid"""
        valid_confidence = reference_codes[reference_codes['field'] == 'confidence']['code'].tolist()
        actual_confidence = enriched_data['confidence'].unique()
        
        for conf in actual_confidence:
            assert conf in valid_confidence, f"Invalid confidence level: {conf}"
    
    def test_observations_have_values(self, enriched_data):
        """Test that observations have numeric values"""
        observations = enriched_data[enriched_data['record_type'] == 'observation']
        
        # Check that observations have numeric values
        assert observations['value_numeric'].notna().all(), "All observations should have numeric values"
        
        # Check that values are reasonable (0-1 for percentages)
        assert (observations['value_numeric'] >= 0).all(), "Values should be non-negative"
        assert (observations['value_numeric'] <= 1).all(), "Values should not exceed 1 (percentage format)"
    
    def test_events_have_no_pillar(self, enriched_data):
        """Test that events have empty pillar field"""
        events = enriched_data[enriched_data['record_type'] == 'event']
        
        # Events should have empty pillar by design
        assert (events['pillar'] == '').all(), "Events should have empty pillar field"
    
    def test_impact_links_structure(self, enriched_data):
        """Test that impact links have required fields"""
        impact_links = enriched_data[enriched_data['record_type'] == 'impact_link']
        
        # Check required fields for impact links
        required_impact_fields = ['parent_id', 'related_indicator', 'impact_direction', 'impact_magnitude', 'lag_months']
        
        for field in required_impact_fields:
            assert field in enriched_data.columns, f"Missing impact link field: {field}"
        
        # Check that impact magnitudes are reasonable
        assert (impact_links['impact_magnitude'] >= 0).all(), "Impact magnitudes should be non-negative"
        assert (impact_links['impact_magnitude'] <= 1).all(), "Impact magnitudes should not exceed 1"
        
        # Check that lag months are reasonable
        assert (impact_links['lag_months'] >= 0).all(), "Lag months should be non-negative"
    
    def test_date_format(self, enriched_data):
        """Test that observation dates are in valid format"""
        # Test observations have dates
        observations = enriched_data[enriched_data['record_type'] == 'observation']
        assert observations['observation_date'].notna().all(), "All observations should have dates"
        
        # Test date format (YYYY-MM-DD or YYYY-MM-DD HH:MM:SS)
        date_pattern = r'^\d{4}-\d{2}-\d{2}'
        assert observations['observation_date'].str.match(date_pattern).all(), "Dates should be in YYYY-MM-DD format"
    
    def test_source_urls(self, enriched_data):
        """Test that records have source URLs where expected"""
        # Observations and events should have source URLs
        observations = enriched_data[enriched_data['record_type'] == 'observation']
        events = enriched_data[enriched_data['record_type'] == 'event']
        
        assert observations['source_url'].notna().all(), "Observations should have source URLs"
        assert events['source_url'].notna().all(), "Events should have source URLs"
        
        # Check URL format
        url_pattern = r'^https?://'
        assert observations['source_url'].str.match(url_pattern).all(), "Source URLs should be valid HTTP/HTTPS URLs"
        assert events['source_url'].str.match(url_pattern).all(), "Source URLs should be valid HTTP/HTTPS URLs"
    
    def test_record_id_uniqueness(self, enriched_data):
        """Test that record IDs are unique"""
        assert enriched_data['record_id'].nunique() == len(enriched_data), "Record IDs should be unique"
    
    def test_indicator_codes_consistency(self, enriched_data):
        """Test that indicator codes are consistent"""
        # Check that same indicator has same indicator_code
        indicator_mapping = enriched_data[['indicator', 'indicator_code']].dropna()
        
        for indicator in indicator_mapping['indicator'].unique():
            codes = indicator_mapping[indicator_mapping['indicator'] == indicator]['indicator_code'].unique()
            assert len(codes) == 1, f"Indicator {indicator} has multiple codes: {codes}"
    
    def test_enrichment_additions(self, enriched_data):
        """Test that enrichment additions are present"""
        # Should have more records than original dataset (18)
        assert len(enriched_data) > 18, "Enriched dataset should have more than 18 records"
        
        # Should have specific enriched indicators
        enriched_indicators = [
            'infra_mobile_penetration',
            'infra_4g_coverage', 
            'infra_smartphone_penetration',
            'access_account_male',
            'access_account_female'
        ]
        
        for indicator in enriched_indicators:
            assert indicator in enriched_data['indicator_code'].values, f"Missing enriched indicator: {indicator}"
        
        # Should have enriched events
        enriched_events = ['policy_mm_regulation', 'infra_4g_launch']
        for event in enriched_events:
            assert event in enriched_data['indicator_code'].values, f"Missing enriched event: {event}"

if __name__ == "__main__":
    pytest.main([__file__])
