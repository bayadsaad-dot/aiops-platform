import { useState } from "react";
import { useParams } from "react-router-dom";

import {
  Box,
  Button,
  Card,
  CardContent,
  CircularProgress,
  LinearProgress,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Stack,
  Typography,
} from "@mui/material";

import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import PsychologyIcon from "@mui/icons-material/Psychology";
import WarningAmberIcon from "@mui/icons-material/WarningAmber";
import DescriptionIcon from "@mui/icons-material/Description";

import { useIncidentAnalysis } from "../hooks/useIncidentAnalysis";

export default function IncidentDetails() {
  const { id } = useParams();

  const { analyze, loading } = useIncidentAnalysis();

  const [analysis, setAnalysis] = useState<any>(null);

  async function handleAnalyze() {
    if (!id) return;

    const result = await analyze(id);

    setAnalysis(result.analysis);
  }

  return (
    <Box p={4}>

      <Stack
        direction="row"
        justifyContent="center"
        alignItems="center"
        mb={4}
      >
        <Typography variant="h3" fontWeight={700}>
          Incident Analysis
        </Typography>

        <Button
          variant="contained"
          size="large"
          onClick={handleAnalyze}
          disabled={loading}
        >
          Analyze with AI
        </Button>
      </Stack>

      {loading && (
        <Stack alignItems="center" py={10}>
          <CircularProgress />
          <Typography mt={2}>
            AI is analyzing the incident...
          </Typography>
        </Stack>
      )}

      {!loading && analysis && (
        <Stack spacing={3}>

          <Card>
            <CardContent>
              <Stack direction="row" spacing={2}>
                <DescriptionIcon color="primary" />

                <Box>
                  <Typography variant="h6">
                    Summary
                  </Typography>

                  <Typography>
                    {analysis.summary}
                  </Typography>
                </Box>
              </Stack>
            </CardContent>
          </Card>

          <Card>
            <CardContent>

              <Stack direction="row" spacing={2}>
                <PsychologyIcon color="error"/>

                <Box>
                  <Typography variant="h6">
                    Root Cause
                  </Typography>

                  <Typography>
                    {analysis.root_cause}
                  </Typography>
                </Box>
              </Stack>

            </CardContent>
          </Card>

          <Card>
            <CardContent>

              <Stack direction="row" spacing={2}>
                <WarningAmberIcon color="warning"/>

                <Box>

                  <Typography variant="h6">
                    Impact
                  </Typography>

                  <Typography>
                    {analysis.impact}
                  </Typography>

                </Box>
              </Stack>

            </CardContent>
          </Card>

          <Card>

            <CardContent>

              <Typography variant="h6" mb={2}>
                Confidence
              </Typography>

              <Typography mb={1}>
                {analysis.confidence}%
              </Typography>

              <LinearProgress
                variant="determinate"
                value={analysis.confidence}
                sx={{
                  height: 12,
                  borderRadius: 10,
                }}
              />

            </CardContent>

          </Card>

          <Card>

            <CardContent>

              <Typography
                variant="h6"
                mb={2}
              >
                Recommendations
              </Typography>

              <List>

                {analysis.recommendations.map(
                  (item: string, index: number) => (
                    <ListItem key={index}>

                      <ListItemIcon>
                        <CheckCircleIcon color="success"/>
                      </ListItemIcon>

                      <ListItemText primary={item}/>

                    </ListItem>
                  )
                )}

              </List>

            </CardContent>

          </Card>

        </Stack>
      )}

    </Box>
  );
}