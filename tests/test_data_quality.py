"""
Data quality tests for Ethiopia Financial Inclusion Forecasting System
"""
import pandas as pd
import pytest
import sys
import os

# Add src directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

class TestDataQuality:
    """Test suite for data quality assessment"""
    
    @pytest.fixture
    def enriched_data(self):
        """Load enriched dataset for testing"""
        data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed', 'ethiopia_fi_enriched_data.csv')
        return pd.read_csv(data_path)
    
    def test_temporal_coverage(self, enriched_data):
        """Test temporal coverage requirements"""
        observations = enriched_data[enriched_data['record_type'] == 'observation'].copy()
        observations['observation_date'] = pd.to_datetime(observations['observation_date'])
        
        # Should have data for key Findex years
        required_years = [2011, 2014, 2017, 2021, 2024]
        available_years = observations['observation_date'].dt.year.unique()
        
        for year in required_years:
            assert year in available_years, f"Missing data for required year: {year}"
    
    def test_account_ownership_completeness(self, enriched_data):
        """Test account ownership data completeness"""
        observations = enriched_data[enriched_data['record_type'] == 'observation']
        account_ownership = observations[observations['indicator_code'] == 'access_account_ownership']
        
        # Should have complete time series
        assert len(account_ownership) >= 5, "Should have at least 5 account ownership data points"
        
        # Values should be in reasonable range
        assert account_ownership['value_numeric'].between(0, 1).all(), "Account ownership should be between 0 and 1"
        
        # Should show growth over time
        account_ownership_sorted = account_ownership.sort_values('observation_date')
        values = account_ownership_sorted['value_numeric'].values
        assert values[-1] > values[0], "Account ownership should show growth over time"
    
    def test_gender_data_quality(self, enriched_data):
        """Test gender-disaggregated data quality"""
        observations = enriched_data[enriched_data['record_type'] == 'observation']
        
        # Should have gender-disaggregated data
        male_data = observations[observations['indicator_code'] == 'access_account_male']
        female_data = observations[observations['indicator_code'] == 'access_account_female']
        
        assert len(male_data) > 0, "Should have male account ownership data"
        assert len(female_data) > 0, "Should have female account ownership data"
        
        # Male ownership should be higher than female
        male_value = male_data['value_numeric'].iloc[0]
        female_value = female_data['value_numeric'].iloc[0]
        assert male_value > female_value, "Male account ownership should be higher than female"
    
    def test_infrastructure_data_plausibility(self, enriched_data):
        """Test infrastructure data plausibility"""
        observations = enriched_data[enriched_data['record_type'] == 'observation']
        
        # Get infrastructure indicators
        mobile_penetration = observations[observations['indicator_code'] == 'infra_mobile_penetration']
        smartphone_penetration = observations[observations['indicator_code'] == 'infra_smartphone_penetration']
        four_g_coverage = observations[observations['indicator_code'] == 'infra_4g_coverage']
        
        # Should have infrastructure data
        assert len(mobile_penetration) > 0, "Should have mobile penetration data"
        assert len(smartphone_penetration) > 0, "Should have smartphone penetration data"
        assert len(four_g_coverage) > 0, "Should have 4G coverage data"
        
        # Plausibility checks
        mobile_value = mobile_penetration['value_numeric'].iloc[0]
        smartphone_value = smartphone_penetration['value_numeric'].iloc[0]
        four_g_value = four_g_coverage['value_numeric'].iloc[0]
        
        # Mobile penetration should be higher than smartphone penetration
        assert mobile_value > smartphone_value, "Mobile penetration should exceed smartphone penetration"
        
        # Values should be reasonable
        assert mobile_value > 0.3, "Mobile penetration should be > 30% for Ethiopia"
        assert smartphone_value > 0.1, "Smartphone penetration should be > 10%"
        assert four_g_value > 0.2, "4G coverage should be > 20%"
    
    def test_event_data_completeness(self, enriched_data):
        """Test event data completeness"""
        events = enriched_data[enriched_data['record_type'] == 'event']
        
        # Should have key events
        required_events = [
            'telebirr_launch',
            'mpesa_launch', 
            'safaricom_entry',
            'nfis_ii_launch'
        ]
        
        for event in required_events:
            assert event in events['indicator_code'].values, f"Missing required event: {event}"
        
        # Events should have dates
        assert events['observation_date'].notna().all(), "All events should have dates"
        
        # Events should have sources
        assert events['source_name'].notna().all(), "All events should have source names"
        assert events['source_url'].notna().all(), "All events should have source URLs"
    
    def test_impact_link_quality(self, enriched_data):
        """Test impact link data quality"""
        impact_links = enriched_data[enriched_data['record_type'] == 'impact_link']
        
        # Should have impact links
        assert len(impact_links) > 0, "Should have impact links"
        
        # Impact magnitudes should be reasonable
        assert impact_links['impact_magnitude'].between(0, 1).all(), "Impact magnitudes should be between 0 and 1"
        
        # Lag months should be reasonable
        assert impact_links['lag_months'].between(0, 60).all(), "Lag months should be between 0 and 60"
        
        # Should have both positive and negative directions (if applicable)
        directions = impact_links['impact_direction'].unique()
        assert 'positive' in directions, "Should have positive impact directions"
    
    def test_data_consistency(self, enriched_data):
        """Test data consistency across records"""
        observations = enriched_data[enriched_data['record_type'] == 'observation']
        
        # Account ownership should be consistent with gender data
        overall = observations[observations['indicator_code'] == 'access_account_ownership']
        male = observations[observations['indicator_code'] == 'access_account_male']
        female = observations[observations['indicator_code'] == 'access_account_female']
        
        if len(overall) > 0 and len(male) > 0 and len(female) > 0:
            overall_value = overall['value_numeric'].iloc[-1]  # Latest value
            male_value = male['value_numeric'].iloc[0]
            female_value = female['value_numeric'].iloc[0]
            
            # Overall should be between male and female (approximate)
            # Allow some tolerance due to different collection methods
            weighted_avg = (male_value + female_value) / 2
            assert abs(overall_value - weighted_avg) < 0.1, "Overall account ownership should be close to gender average"
    
    def test_missing_data_patterns(self, enriched_data):
        """Test for patterns in missing data"""
        # Check that missing data is systematic rather than random
        missing_by_record_type = enriched_data.isnull().groupby(enriched_data['record_type']).sum()
        
        # Impact links should have missing value_numeric (by design)
        impact_links = enriched_data[enriched_data['record_type'] == 'impact_link']
        assert impact_links['value_numeric'].isna().all(), "Impact links should not have value_numeric"
        
        # Events should have missing value_numeric (by design)
        events = enriched_data[enriched_data['record_type'] == 'event']
        assert events['value_numeric'].isna().all(), "Events should not have value_numeric"
    
    def test_source_diversity(self, enriched_data):
        """Test source diversity for data reliability"""
        # Should have multiple sources
        unique_sources = enriched_data['source_name'].nunique()
        assert unique_sources >= 3, f"Should have at least 3 different sources, found {unique_sources}"
        
        # Should have reputable sources
        reputable_sources = [
            'Global Findex',
            'National Bank of Ethiopia', 
            'Ethio Telecom',
            'Ethiopia Communication Authority',
            'GSMA Mobile Economy'
        ]
        
        for source in reputable_sources:
            assert source in enriched_data['source_name'].values, f"Missing reputable source: {source}"
    
    def test_confidence_distribution(self, enriched_data):
        """Test confidence level distribution"""
        confidence_counts = enriched_data['confidence'].value_counts()
        
        # Should have high confidence data
        assert 'high' in confidence_counts, "Should have high confidence data"
        
        # Most data should be high or medium confidence
        high_medium_pct = (confidence_counts.get('high', 0) + confidence_counts.get('medium', 0)) / len(enriched_data)
        assert high_medium_pct > 0.7, "At least 70% of data should be high or medium confidence"

if __name__ == "__main__":
    pytest.main([__file__])
