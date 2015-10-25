from django import forms

from .models import TeamMatch, Team

from collections import defaultdict

class MatchForm(forms.ModelForm):
    class Meta:
        model = TeamMatch
        fields = ['ring_number', 'winning_team']

class SeedingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['seed'].label = str(self.instance)

    class Meta:
        model = Team
        fields = ['id', 'seed']

    @staticmethod
    def all_seeds_valid(seed_forms):
        errors = []
        modified_teams = [form.save(commit=False) for form in seed_forms]
        for team in modified_teams:
            if team.seed is None: continue
            if team.seed >= 1: continue
            errors.append(forms.ValidationError("Team " + str(team) + " has"
                    + " seed < 1 (%d)" %team.seed))
        divisions = {form_team.division for form_team in modified_teams}
        if len(divisions) > 1:
            errors.append(forms.ValidationError("Cannot handle teams from"
                    + " multiple divisions (teams supplied have %s)"
                    %(divisions)))
            raise forms.ValidationError(errors)
        division = divisions.pop()

        teams = {t.id:t for t in Team.objects.filter(division=division)}
        for team in modified_teams:
            teams[team.id] = team
        filled_seeds = defaultdict(list)
        for team in teams.values():
            if team.seed is None: continue
            filled_seeds[team.seed].append(team)
        duplicated_seeds = {seed:teams for seed,teams in filled_seeds.items()
                if len(teams) > 1}
        if duplicated_seeds:
            errors.append(forms.ValidationError("The following seeds have"
                    + " multiple teams assigned: " + str(duplicated_seeds)))
        if errors:
            raise forms.ValidationError(errors)
