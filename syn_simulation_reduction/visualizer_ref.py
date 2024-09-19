"""
The Visualizer class.
"""
import pathlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import seaborn as sns
import cv2 as cv
import numpy as np

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import config

from utility import BoundingBox, Detection, Image, Sequence, Parameters, Metrics, PandaReader, PTZActuatorReader
from typing import ClassVar, Generator, Optional, List, Tuple, Dict


class Visualizer:
    Color = Tuple[float, float, float]

    SEED: ClassVar[int] = 123456789
    CLASS_COUNT: ClassVar[int] = 80
    RNG: ClassVar[Generator] = np.random.default_rng(seed=SEED)
    COLOR_MAP: ClassVar[np.ndarray] = RNG.uniform(0.0, 255.0, size=(CLASS_COUNT, 3))
    PREDICTION_COLOR: ClassVar[Color] = (255.0, 64.0, 64.0)
    GROUND_TRUTH_COLOR: ClassVar[Color] = (64.0, 255.0, 64.0)
    BOX_SIZE: ClassVar[int] = 25

    @staticmethod
    def visualize(image: Image, detections: List[Detection], box_color: Optional[Color] = None) -> Image:
        output = image.copy()

        def draw_box(detection: Detection) -> None:
            class_label = f"{detection.label} [{detection.class_id}]" if detection.label else f"{detection.class_id}"
            label = f"{class_label} ({detection.confidence:.2f})"
            color = box_color or Visualizer.COLOR_MAP[detection.class_id]
            color = color[2], color[1], color[0]
            box = detection.bounding_box
            cv.rectangle(output.data, box.top_left, box.bottom_right, color, Visualizer.BOX_SIZE)
            #cv.putText(output.data, label, (box.x - 10, box.y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        list(map(draw_box, detections))
        return output

    @staticmethod
    def visualize_predictions(image: Image, detections: List[Detection]) -> Image:
        return Visualizer.visualize(image, detections, Visualizer.PREDICTION_COLOR)

    @staticmethod
    def visualize_ground_truth(image: Image, detections: List[Detection]) -> Image:
        return Visualizer.visualize(image, detections, Visualizer.GROUND_TRUTH_COLOR)

    @staticmethod
    def visualize_tiles(image: Image, tiles: List[BoundingBox]) -> Image:
        output = image.copy()
        for index, box in enumerate(tiles):
            color = Visualizer.COLOR_MAP[index]
            color = color[2], color[1], color[0]
            cv.rectangle(output.data, box.top_left, box.bottom_right, color, Visualizer.BOX_SIZE)
        return output

    @staticmethod
    def plot_graphs(ay_indexes: Tuple[float, float], ax_indexes: Tuple[float, float], x_series: np.ndarray,
                    y_series: np.ndarray, ax_name: str, ay_name: str, legend: List[str],
                    output_path: pathlib.Path, file_name:Optional[str] = None, graph_name: Optional[str] = None,
                    series_labels: Optional[List[List[str]]] = None,
                    lines: Optional[Dict[str, List[Tuple[str, float]]]] = None,
                    color_list: Optional[List[int]] = None, pattern: Optional[str] = "colorblind",
                    loca: Optional[str] = 'center left', numcol: Optional[int] = 3,
                    axticks: Optional[List[int]] = None, size_of_pallete: Optional[int] = 10,
                    marker_list: Optional[List[str]] = None):
        palette = sns.color_palette(pattern, size_of_pallete)
        _, ax = plt.subplots()
        axis_limits = [ax_indexes[0], ax_indexes[1], ay_indexes[0], ay_indexes[1]]

        if color_list is None and size_of_pallete == 10:
            colors = ['red', 'green', 'orange', 'purple', 'brown', 'gray']
        elif color_list is not None:
            colors = color_list
        else:
            colors = palette
        legend_lines = list()
        if marker_list is not None:
            markers = marker_list
        else:
            markers = ['. ' for _ in range(len(legend_lines))]
        # Do plots
        for serie_index, (x_serie, y_serie, strategy, marker) in enumerate(zip(x_series, y_series, legend, markers)):
            ax.plot(x_serie, y_serie, color=colors[serie_index % len(colors)],  marker=marker, label=strategy)
            if marker == '.':
                legend_lines.append(mlines.Line2D([], [], color=colors[serie_index % len(colors)], linestyle='-',
                                                  linewidth=4, markersize=16, marker=marker, label=strategy))
            else:
                legend_lines.append(mlines.Line2D([], [], color=colors[serie_index % len(colors)], linestyle='-',
                                    linewidth=4, markersize=10, marker=marker, label=strategy))
            if series_labels is not None:
                    for x, y, value in zip(x_serie, y_serie, series_labels[serie_index]):
                        ax.annotate(value, xy=(x, y), xytext=(5, -10), textcoords='offset points')
        if lines is not None:
            for color_index, (orientation, positions) in enumerate(lines.items()):
                if orientation == "h":
                    for position in positions:
                        ax.axhline(y=position[1], xmin=axis_limits[0], xmax=axis_limits[1] * 0.8,
                                    color='black')
                        plt.text(axis_limits[1] * 0.8, position[1], position[0], rotation=0, verticalalignment='center')
                else:
                    for position in positions:
                        ax.axvline(x=position[1], ymin=axis_limits[2], ymax=axis_limits[3] * 0.8,
                                    color='black')
                        plt.text(position[1], axis_limits[3] * 0.8, position[0], rotation=0, verticalalignment='center')
        # Write parameters and labels
        if loca == 'center left':
            plt.legend(handles=legend_lines, loc='center left', bbox_to_anchor=(1, 0.5),fontsize=14)
        else:
            plt.legend(handles=legend_lines, loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=numcol, fontsize=14)
        plt.axis(axis_limits)
        plt.xlabel(ax_name, fontsize=16)
        plt.ylabel(ay_name, fontsize=16)
        plt.setp(ax.get_xticklabels(), fontsize=12)
        plt.setp(ax.get_yticklabels(), fontsize=12)
        plt.title(graph_name, fontsize=16)
        if axticks is not None:
            plt.xticks(axticks)

        if file_name is not None:
            file_name = f"{file_name}.pdf"
        else:
            file_name = f"{graph_name}.pdf"
        plt.savefig(output_path / "figures" / file_name, bbox_inches='tight')

    @staticmethod
    def plot_historical(x_series: np.ndarray, y_series: np.ndarray, legend: [List[str], List[str]],
                        improv_matrix: np.ndarray, output_path: pathlib.Path, file_name: Optional[str] = None,
                        graph_name: Optional[str] = None, color_list: [List[str], List[str]] = None,
                        marker_list: Optional[List[str]] = None):

        config.configure(mpl, plt)

        fig, axs = plt.subplots(1, 2, figsize=config.set_size(config.width, height_div=3, fraction=0.5))
        colors = color_list[0]
        legend_lines = list()
        if marker_list is not None:
            markers = marker_list
        else:
            markers = ['. ' for _ in range(len(legend_lines))]
        # Do plots
        for serie_index, (x_serie, y_serie, strategy, marker, color) in enumerate(zip(x_series, y_series, legend[0],
                                                                                      markers, colors)):
            axs[0].plot(x_serie, y_serie, color=color, marker=marker, markersize=3, label=strategy/1000)
            legend_lines.append(mlines.Line2D([], [], color=colors[serie_index % len(colors)], linestyle='-',
                                              linewidth=1.25, markersize=6, marker=marker, label=strategy/1000))

        lege = axs[0].legend(handles=legend_lines, loc='lower center', bbox_to_anchor=(0.5, 0), fontsize=10, ncol = 3)
        lege.get_frame().set_alpha(0.5)
        axs[0].set_ylim(5, 24)
        axs[0].set_xlim(9, 31)
        axs[0].set_xlabel("Historical Frame Count (\%)", fontsize=14)
        axs[0].set_ylabel("mAP (\%)", fontsize=14)
        axs[0].tick_params(axis='x', labelsize=12)
        axs[0].tick_params(axis='y', labelsize=12)
        axs[0].set_title("Historical Frame Performance", fontsize=14)

        #####

        num_budgets = len(legend[0])
        num_sequences = len(legend[1])

        bar_width = 0.8 / num_sequences

        indices = np.arange(num_budgets)

        colors = color_list[1]

        for (i, seq), color in zip(enumerate(legend[1]), colors):
            seq_values = [improv_matrix[i][j]*100 for j in range(num_budgets)]
            bar_positions = indices + i * bar_width
            axs[1].bar(bar_positions, seq_values, bar_width, label=seq, edgecolor='black', color=color)

        axs[1].set_xticks(indices + (num_sequences - 1) * bar_width / 2)
        axs[1].set_xticklabels([budget/1000 for budget in legend[0]])
        axs[1].set_ylim(5, 25)

        # Add labels and title
        axs[1].set_xlabel('Latency SLOs (s)', fontsize=14)
        axs[1].set_xticklabels(axs[1].get_xticklabels(), rotation=45, ha='right')
        #axs[1].set_ylabel('mAP (\%)', fontsize=14)
        axs[1].tick_params(axis='x', labelsize=12)
        axs[1].tick_params(axis='y', labelsize=12)
        axs[1].set_title('Object\'s Extraction', fontsize=14)
        axs[1].legend(fontsize=10, loc='upper left', ncol=1, bbox_to_anchor=(0, 1))

        if file_name is not None:
            file_name = f"{file_name}"
        else:
            file_name = f"{graph_name}"
        fig.savefig(output_path / "figures" / file_name, format="pdf", dpi=config.dpi, bbox_inches='tight')

    @staticmethod
    def plot_model_dist(ay_indexes: Tuple[float, float], budgets: List[int], sequences: List[str],
                                    improv_matrix: np.ndarray, output_path: pathlib.Path,
                                    ax_name: str, ay_name: str, tile: str,
                                    file_name: Optional[str] = None, graph_name: Optional[str] = None,
                                    color_list: Optional[List[int]] = None,
                                    pattern: Optional[str] = "colorblind", a_o: Optional[bool] = False,
                                    color_type: bool = False):

        config.configure(mpl, plt)
        num_budgets = len(budgets)
        num_sequences = len(sequences)
        sns.set_palette(pattern, 10)
        fig, ax = plt.subplots(figsize=config.set_size(config.width, height_div=3, fraction=0.5))

        bar_width = 0.8 / num_sequences

        indices = np.arange(num_budgets)

        if color_list is not None:
            if color_type:
                colors = color_list
            else:
                palette = sns.color_palette(pattern, 10)
                colors = [palette[index] for index in color_list]
            for (i, seq), color in zip(enumerate(sequences), colors):
                seq_values = [improv_matrix[j][i] for j in range(num_budgets)]
                bar_positions = indices + i * bar_width
                ax.bar(bar_positions, seq_values, bar_width, label=seq, edgecolor='black', color=color)
        else:
            for i, seq in enumerate(sequences):
                seq_values = [improv_matrix[j][i] for j in range(num_budgets)]
                bar_positions = indices + i * bar_width
                ax.bar(bar_positions, seq_values, bar_width, label=seq, edgecolor='black')
        if a_o:
            ax.legend(title="Sequences", fontsize=14)
            ax.axhline(y=0, color='black', linewidth=1.5, linestyle='-')
        ax.set_xticks(indices + (num_sequences - 1) * bar_width / 2)
        ax.set_xticklabels(budgets)
        ax.set_ylim(ay_indexes)

        # Add labels and title
        ax.set_xlabel(ax_name, fontsize=14)
        ax.set_ylabel(ay_name, fontsize=14)
        ax.tick_params(axis='x', labelsize=12)
        ax.tick_params(axis='y', labelsize=12)
        #ax.set_title(tile, fontsize=14)
        legend = ax.legend(fontsize=10, loc='upper left', ncol=4, bbox_to_anchor=(0, 1.03))
        legend.set_frame_on(False)


        # Show the plot
        if file_name is not None:
            file_name = f"{file_name}"
        else:
            file_name = f"{graph_name}"

        fig.savefig(output_path / "figures" / file_name, format="pdf", dpi=config.dpi, bbox_inches='tight')

    @staticmethod
    def plot_stacked_timings(ay_indexes: Tuple[float, float], budgets: List[int], sequences: List[str],
                                 improv_matrix: np.ndarray, output_path: pathlib.Path,
                                 ax_name: str, ay_name: str, tile: str,
                                 file_name: Optional[str] = None, graph_name: Optional[str] = None,
                                 color_list: Optional[List[str]] = None):

        config.configure(mpl, plt)
        num_budgets = len(budgets)
        fig, ax = plt.subplots(figsize=config.set_size(config.width, height_div=3, fraction=0.5))

        bar_width = 0.8
        indices = np.arange(num_budgets)

        bottom_values = np.zeros(num_budgets)

        if color_list is not None:
            for i, (seq, color) in enumerate(zip(sequences, color_list)):
                seq_values = np.array([improv_matrix[j][i] for j in range(num_budgets)])
                ax.bar(indices, seq_values, bar_width, label=seq, color=color, edgecolor='black', bottom=bottom_values)
                bottom_values += seq_values
        else:
            for i, seq in enumerate(sequences):
                seq_values = np.array([improv_matrix[j][i] for j in range(num_budgets)])
                ax.bar(indices, seq_values, bar_width, label=seq, edgecolor='black', bottom=bottom_values)
                bottom_values += seq_values

        ax.set_xticks(indices)
        ax.set_xticklabels(budgets)
        ax.set_ylim(ay_indexes)

        # Add labels and title
        ax.set_xlabel(ax_name, fontsize=14)
        ax.set_ylabel(ay_name, fontsize=14)
        ax.tick_params(axis='x', labelsize=12)
        ax.tick_params(axis='y', labelsize=12)
        #ax.set_title(tile, fontsize=14)
        ax.legend(fontsize=12)

        # Save the plot
        if file_name is not None:
            file_name = f"{file_name}"
        else:
            file_name = f"{graph_name}"

        fig.savefig(output_path / "figures" / file_name, format="pdf", dpi=config.dpi, bbox_inches='tight')
    @staticmethod
    def breackdown_visualization(ay_indexes: Tuple[float, float], ax_indexes: Tuple[float, float], x_1: np.ndarray,
                                 x_2: np.ndarray, x_3: np.ndarray, y_1: np.ndarray, y_2: np.ndarray,
                                 y_3: np.ndarray, ax_name: str, ay_name: str, legend: List[str],
                                 output_path: pathlib.Path, graph_name_1: [str], graph_name_2: [str],
                                 graph_name_3: [str], markers: List[str],
                                 file_name: Optional[str] = None,
                                 series_labels: Optional[List[List[str]]] = None,
                                 lines_1: Optional[Dict[str, List[Tuple[str, float]]]] = None,
                                 lines_2: Optional[Dict[str, List[Tuple[str, float]]]] = None,
                                 lines_3: Optional[Dict[str, List[Tuple[str, float]]]] = None,
                                 color_list: Optional[List[str]] = None):

        config.configure(mpl, plt)
        if color_list is None:
            colors = ['red', 'green', 'orange', 'purple', 'brown', 'gray']
        else:
            colors = color_list

        # Create a figure and a grid for subplots
        fig, axs = plt.subplots(3, 1, figsize=config.set_size(config.width, height_div=1, fraction=0.5))
        fig.tight_layout(pad=2)

        axis_limits = [ax_indexes[0], ax_indexes[1], ay_indexes[0], ay_indexes[1]]

        if colors is None:
            colors = ['red', 'green', 'orange', 'purple', 'brown', 'gray']
        # Plotting the first figure
        axs[0].set_title(graph_name_1, fontsize=16)
        axs[0].set_xlim(axis_limits[0], axis_limits[1])
        axs[0].set_ylim(10, 50)
        axs[0].tick_params(axis='x', labelsize=14)
        axs[0].tick_params(axis='y', labelsize=14)
        legend_lines = list()
        for serie_index, (x_serie, y_serie, strategy, marker) in enumerate(zip(x_1, y_1, legend, markers)):
            axs[0].plot(x_serie, y_serie, color=colors[serie_index % len(colors)], linestyle='--',
                        marker=marker, label=strategy, linewidth=1.25, markersize=3)
            legend_lines.append(mlines.Line2D([], [], color=colors[serie_index % len(colors)], linestyle='--',
                                linewidth=1.25, markersize=6, marker=marker, label=strategy))
            if series_labels is not None:
                for x, y, value in zip(x_serie, y_serie, series_labels[serie_index]):
                    axs[0].annotate(value, xy=(x, y), xytext=(5, -10), textcoords='offset points')
        if lines_1 is not None:
            for color_index, (orientation, positions) in enumerate(lines_1.items()):
                if orientation == "h":
                    for position in positions:
                        axs[0].axhline(y=position[1], xmin=axis_limits[0], xmax=axis_limits[1] * 0.8,
                                    color='black')
                        axs[0].text(axis_limits[1] * 0.8, position[1], position[0], rotation=0,
                                    verticalalignment='center', fontsize=12)
                else:
                    for position in positions:
                        axs[0].axvline(x=position[1], ymin=axis_limits[2], ymax=axis_limits[3] * 0.8,
                                    color='black')
                        axs[0].text(position[1] + 2, 50 * 0.9, position[0], rotation=0,
                                    verticalalignment='center', fontsize=12)

        # Plotting the second figure
        axs[1].set_title(graph_name_2, fontsize=16)
        axs[1].set_xlim(axis_limits[0], axis_limits[1])
        axs[1].set_ylim(axis_limits[2], axis_limits[3])
        axs[1].set_ylabel(ay_name, fontsize=22)
        axs[1].tick_params(axis='x', labelsize=14)
        axs[1].tick_params(axis='y', labelsize=14)
        #axs[1].set_ylabel(ay_name)
        for serie_index, (x_serie, y_serie, strategy, marker) in enumerate(zip(x_2, y_2, legend, markers)):
            axs[1].plot(x_serie, y_serie, color=colors[serie_index % len(colors)], linestyle='--',
                        marker=marker, label=strategy, linewidth=1.25, markersize=3)
            if series_labels is not None:
                for x, y, value in zip(x_serie, y_serie, series_labels[serie_index]):
                    axs[1].annotate(value, xy=(x, y), xytext=(5, -10), textcoords='offset points')
        if lines_2 is not None:
            for color_index, (orientation, positions) in enumerate(lines_2.items()):
                if orientation == "h":
                    for position in positions:
                        axs[1].axhline(y=position[1], xmin=axis_limits[0], xmax=axis_limits[1] * 0.8,
                                        color='black')
                        axs[1].text(axis_limits[1] * 0.9, position[1], position[0], rotation=0,
                                    verticalalignment='center', fontsize=12)
                else:
                    for position in positions:
                        axs[1].axvline(x=position[1], ymin=axis_limits[2], ymax=axis_limits[3] * 0.8,
                                        color='black')
                        axs[1].text(position[1] + 2, axis_limits[3] * 0.8, position[0], rotation=0,
                                    verticalalignment='center', fontsize=12)
        # Plotting the third figure
        axs[2].set_title(graph_name_3, fontsize=16)
        axs[2].set_xlim(axis_limits[0], axis_limits[1])
        axs[2].set_ylim(axis_limits[2], 60)
        axs[2].set_xlabel(ax_name, fontsize=22)
        axs[2].tick_params(axis='x', labelsize=14)
        axs[2].tick_params(axis='y', labelsize=14)
        #axs[2].set_ylabel(ay_name)
        for serie_index, (x_serie, y_serie, strategy, marker) in enumerate(zip(x_3, y_3, legend, markers)):
            axs[2].plot(x_serie, y_serie, color=colors[serie_index % len(colors)], linestyle='--',
                        marker=marker, label=strategy, linewidth=1.25, markersize=3)
            if series_labels is not None:
                for x, y, value in zip(x_serie, y_serie, series_labels[serie_index]):
                    axs[2].annotate(value, xy=(x, y), xytext=(5, -10), textcoords='offset points')
        if lines_3 is not None:
            for color_index, (orientation, positions) in enumerate(lines_3.items()):
                if orientation == "h":
                    for position in positions:
                        axs[2].axhline(y=position[1], xmin=axis_limits[0], xmax=axis_limits[1] * 0.8,
                                        color='black')
                        axs[2].text(axis_limits[1] * 0.8, position[1], position[0], rotation=0,
                                    verticalalignment='center', fontsize=12)
                else:
                    for position in positions:
                        axs[2].axvline(x=position[1], ymin=axis_limits[2], ymax=axis_limits[3] * 0.8,
                                        color='black')
                        axs[2].text(position[1] + 2, 60 * 0.9, position[0], rotation=0,
                                    verticalalignment='center', fontsize=12)

        # Remove individual legends
        for ax in axs:
            ax.legend().remove()

        # Add a unique legend below all plots
        handles, labels = axs[0].get_legend_handles_labels()
        fig.legend(legend_lines, labels, loc='upper center', ncol=4, fontsize=14, bbox_to_anchor=(0.5, 1.03))

        # Adjust the spacing around the plots and the legend
        #plt.subplots_adjust(bottom=0.2)

        # Write parameters and labels
        fig.savefig(output_path / "figures" / file_name, format="pdf", dpi=config.dpi, bbox_inches='tight')

    @staticmethod
    def profile_visualization(ax_ticks: List[List[str]],
                              x_1: np.ndarray, x_2: np.ndarray, y_1: np.ndarray, y_2: np.ndarray,
                              ay_name: str, legend: List[str],markers: List[str],
                              output_path: pathlib.Path,
                              file_name: Optional[str] = None,
                              color_list: Optional[List[int]] = None):
        config.configure(mpl, plt)

        if color_list is None:
            colors = ['red', 'green', 'orange', 'purple', 'brown', 'gray']
        else:
            colors = color_list

        # Create a figure and a grid for subplots
        fig, axs = plt.subplots(1, 2, figsize=config.set_size(config.width, height_div=4, fraction=0.5))
        #fig, axs = plt.subplots(1, 2, figsize=(30, 10), gridspec_kw={'width_ratios': [1, 1]})
        #fig.tight_layout(pad=4.5)


        # Plotting the first figure
        axs[0].set_xlabel("Absolute area sizes ($pixel^{2}$)", fontsize=14)
        axs[0].set_xlim(0, 12)
        axs[0].set_ylim(0, 60)
        axs[0].set_ylabel(ay_name, fontsize=14)
        axs[0].set_xticks([0, 2, 4, 6, 8, 10])
        axs[0].set_xticklabels(ax_ticks[0], rotation=45, ha='right')
        axs[0].tick_params(axis='x', labelsize=12)
        axs[0].tick_params(axis='y', labelsize=12)
        legend_lines = list()
        for serie_index, (x_serie, y_serie, strategy, marker) in enumerate(zip(x_1, y_1, legend, markers)):
            axs[0].plot(x_serie, y_serie, color=colors[serie_index % len(colors)], marker=marker, label=strategy,
                        linewidth=1.25, markersize=3)
            legend_lines.append(mlines.Line2D([], [], color=colors[serie_index % len(colors)], linestyle='-',
                                linewidth=1.25, markersize=6, marker=marker, label=strategy))

        # Plotting the second figure
        axs[1].set_xlabel("Relative sizes ($\%$)", fontsize=14)
        axs[1].set_xlim(0, 22)
        axs[1].set_ylim(0, 50)
        axs[1].set_xticks([0, 3, 6, 9,
                           12, 15, 18, 21])
        axs[1].set_xlim(left=0, right=25)
        axs[1].set_xticklabels(ax_ticks[1], rotation=45, ha='right')
        axs[1].tick_params(axis='x', labelsize=12)
        axs[1].tick_params(axis='y', labelsize=12)
        # axs[1].set_ylabel(ay_name)
        for serie_index, (x_serie, y_serie, strategy, marker) in enumerate(zip(x_2, y_2, legend, markers)):
            axs[1].plot(x_serie, y_serie, color=colors[serie_index % len(colors)], marker=marker, label=strategy,
                        linewidth=1.25, markersize=3)
        # Plotting the third figure

        # Remove individual legends
        for ax in axs:
            ax.legend().remove()

        # Add a unique legend below all plots
        handles, labels = axs[0].get_legend_handles_labels()
        fig.legend(legend_lines, labels, loc='center right', ncol=1, fontsize=10, bbox_to_anchor=(0.9, 0.5))

        #fig.tight_layout(pad=0.5)
        # Write parameters and labels
        fig.savefig(output_path / "figures" / file_name, format="pdf", dpi=config.dpi, bbox_inches='tight')
        #plt.savefig(output_path / "figures" / (file_name+'.pdf'), bbox_inches='tight')

    @staticmethod
    def double_overall_visualization(ay_ticks: List[int], ax_ticks: List[int],
                                     x_1: np.ndarray, x_2: np.ndarray, y_1: np.ndarray, y_2: np.ndarray,
                                     title1: str, title2: str,
                                     ay_name: str, ax_name: str, legend: List[str], markers: List[str],
                                     output_path: pathlib.Path,
                                     file_name: Optional[str] = None,
                                     color_list: Optional[List[int]] = None, col_num: Optional[int] =1):
        config.configure(mpl, plt)

        if color_list is None:
            colors = ['red', 'green', 'orange', 'purple', 'brown', 'gray']
        else:
            colors = color_list

        # Create a figure and a grid for subplots
        fig, axs = plt.subplots(1, 2, figsize=config.set_size(config.width, height_div=4, fraction=0.5))
        # fig, axs = plt.subplots(1, 2, figsize=(30, 10), gridspec_kw={'width_ratios': [1, 1]})
        # fig.tight_layout(pad=4.5)

        # Plotting the first figure
        axs[0].set_xlabel(ax_name, fontsize=14)
        axs[0].set_xlim(0, ax_ticks[0])
        axs[0].set_ylim(ay_ticks[0], 25)
        axs[0].set_ylabel(ay_name, fontsize=14)
        axs[0].set_title(title1, fontsize=18)
        #axs[0].tick_params(axis='x', labelsize=14)
        #axs[0].tick_params(axis='y', labelsize=14)
        legend_lines = list()
        for serie_index, (x_serie, y_serie, strategy, marker) in enumerate(zip(x_1, y_1, legend, markers)):
            axs[0].plot(x_serie, y_serie, color=colors[serie_index % len(colors)], marker=marker, label=strategy,
                        linewidth=1.25, markersize=3)
            legend_lines.append(mlines.Line2D([], [], color=colors[serie_index % len(colors)], linestyle='-',
                                              linewidth=1.25, markersize=3, marker=marker, label=strategy))

        axs[0].legend(legend_lines, [line.get_label() for line in legend_lines], loc='lower right', ncol=col_num,
                            fontsize=8, bbox_to_anchor=(1, 0))
        # Plotting the second figure
        axs[1].set_xlabel(ax_name, fontsize=14)
        axs[1].set_xlim(0, ax_ticks[1])
        axs[1].set_ylim(ay_ticks[0], 25)
        axs[1].set_title(title2, fontsize=18)
        #axs[1].tick_params(axis='x', labelsize=14)
        #axs[1].tick_params(axis='y', labelsize=14)
        # axs[1].set_ylabel(ay_name)
        for serie_index, (x_serie, y_serie, strategy, marker) in enumerate(zip(x_2, y_2, legend, markers)):
            axs[1].plot(x_serie, y_serie, color=colors[serie_index % len(colors)], marker=marker, label=strategy,
                        linewidth=1.25, markersize=3)

        axs[1].legend(legend_lines, [line.get_label() for line in legend_lines], loc='lower right', ncol=col_num,
                            fontsize=8, bbox_to_anchor=(1, 0))


        # fig.tight_layout(pad=0.5)
        # Write parameters and labels
        fig.savefig(output_path / "figures" / file_name, format="pdf", dpi=config.dpi, bbox_inches='tight')
        # plt.savefig(output_path / "figures" / (file_name+'.pdf'), bbox_inches='tight')

    @staticmethod
    def save_visualization(sequence_path: pathlib.Path, output_path: pathlib.Path, metrics: List[Metrics],
                           parameters: Parameters, detections: List[List[Detection]], fps: Optional[int] = 15):
        full_sequence = Sequence(reader=PandaReader, actuator=PTZActuatorReader)
        full_sequence.load_from_path(sequence_path)
        evaluation_sequence = full_sequence.slice(full_sequence.count - len(detections), full_sequence.count)
        output_file = output_path / (parameters.get_name(sequence_name=sequence_path.name)+".avi")
        video_writer = cv.VideoWriter(str(output_file), cv.VideoWriter.fourcc(*'MJPG'), fps, evaluation_sequence.get_resolution)
        for frame_index, ((frame, labels, actuation, frame_name), frame_detections_list, metric) in enumerate(
                zip(evaluation_sequence.iterate(), detections, metrics)):
            new_frame = frame.copy()
            if hasattr(metric, "partitions_executed"):
                partitions_bounding_boxes = list()
                sub_img = frame.data
                black_rect = np.ones(sub_img.shape, dtype=np.uint8)
                red_rect = black_rect*[0, 0, 255]
                # create opaque red rectangle on the image
                res = cv.addWeighted(sub_img, 0.7, red_rect.astype(np.uint8), 0.3, 1.0)
                # Putting the image back to its position
                new_frame.data[:, :] = res.data
                for partition in metric.partitions_executed:
                    x, y, w, h = partition.bounding_box.x, partition.bounding_box.y, partition.bounding_box.width, \
                        partition.bounding_box.height
                    partitions_bounding_boxes.append(partition.bounding_box)
                    new_frame.data[y:y + h, x:x + w] = frame.data[y:y + h, x:x + w]
                    cv.putText(new_frame.data, str(partition.network_id.split("efficientdet-")[1]), (x, y+70),
                               cv.FONT_HERSHEY_SIMPLEX, 3.0, (255, 255, 255), 3)
                plan_tile_image = Visualizer.visualize_tiles(new_frame, partitions_bounding_boxes)
                labels_image = Visualizer.visualize_ground_truth(plan_tile_image, labels)
            else:
                labels_image = Visualizer.visualize_ground_truth(new_frame, labels)
            prediction_image = Visualizer.visualize_predictions(labels_image, frame_detections_list)
            video_writer.write(prediction_image.data)
            # save_file = output_path / (parameters.get_name(sequence_name=sequence.name) + f"_{frame_name}.pdf")
            # prediction_image.to_file(pathlib.Path(save_file))
        video_writer.release()

